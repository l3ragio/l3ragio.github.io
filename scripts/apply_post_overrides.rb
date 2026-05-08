# scripts/apply_post_overrides.rb
# Re-applies front-matter overrides from _data/post_overrides.yml to
# Medium-synced posts in _posts/zmediumtomarkdown/.
#
# Run after ZMediumToMarkdown so user-curated fields (categories, pin,
# custom tags) survive the monthly overwrite.

require "yaml"
require "date"

POSTS_DIR     = "_posts/zmediumtomarkdown"
OVERRIDES_YML = "_data/post_overrides.yml"
ALLOWED_KEYS  = %w[categories tags pin image_alt].freeze

def split_front_matter(text)
  parts = text.split(/^---\s*$\n/, 3)
  return [nil, text] unless parts.length >= 3 && parts[0].strip.empty?
  [parts[1], parts[2]]
end

def load_yaml(yaml_str, path)
  YAML.safe_load(yaml_str, permitted_classes: [Date, Time], aliases: true) || {}
rescue => e
  warn "YAML parse error in #{path}: #{e}"
  {}
end

def dump_yaml(hash)
  hash.to_yaml.sub(/\A---\s*\n/, "")
end

def slug_from_filename(filename)
  base = File.basename(filename, ".md")
  base.sub(/\A\d{4}-\d{2}-\d{2}-/, "")
end

unless File.exist?(OVERRIDES_YML)
  warn "No #{OVERRIDES_YML} — nothing to apply."
  exit 0
end

unless Dir.exist?(POSTS_DIR)
  warn "No #{POSTS_DIR}/ — nothing to apply."
  exit 0
end

overrides = YAML.safe_load(File.read(OVERRIDES_YML), permitted_classes: [Date, Time]) || {}

changed = 0
matched = 0
missing = overrides.keys.dup

Dir.glob(File.join(POSTS_DIR, "*.md")).sort.each do |path|
  slug = slug_from_filename(path)
  next unless overrides.key?(slug)

  matched += 1
  missing.delete(slug)

  text = File.read(path, mode: "r:bom|utf-8")
  fm_str, body = split_front_matter(text)
  next unless fm_str

  fm = load_yaml(fm_str, path)
  ov = overrides[slug] || {}

  applied = false
  ov.each do |k, v|
    next unless ALLOWED_KEYS.include?(k)
    if fm[k] != v
      fm[k] = v
      applied = true
    end
  end

  next unless applied

  new_text = +"---\n#{dump_yaml(fm)}---\n#{body}"
  File.write(path, new_text)
  changed += 1
end

puts "Overrides matched: #{matched}/#{overrides.size}"
puts "Posts updated:    #{changed}"
unless missing.empty?
  warn "Override slugs with no matching post (Medium post may have been deleted):"
  missing.each { |s| warn "  - #{s}" }
end
