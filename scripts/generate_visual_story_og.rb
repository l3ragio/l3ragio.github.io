# scripts/generate_visual_story_og.rb
# Generates OG preview contact sheets for Visual Stories and sets `image:` in front matter.
#
# Output:
#   assets/og/<slug>.jpg
# Front matter:
#   image: /assets/og/<slug>.jpg
#
# Requirements (CI):
#   - ImageMagick installed (montage, convert)

require "yaml"
require "fileutils"
require "open3"

VISUAL_STORIES_DIR = "_visual_stories"
OUTPUT_DIR         = "assets/og"
MAX_PANELS         = (ENV["OG_MAX_PANELS"] || "6").to_i
TILE_COLS          = (ENV["OG_TILE_COLS"] || "3").to_i
OUT_W              = (ENV["OG_WIDTH"] || "1200").to_i
OUT_H              = (ENV["OG_HEIGHT"] || "630").to_i
QUALITY            = (ENV["OG_QUALITY"] || "82").to_i

def split_front_matter(text)
  # Returns [front_matter_string_or_nil, body_string]
  parts = text.split(/^---\s*$\n/, 3)
  # If file begins with '---\n', split yields: ["", fm, body]
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
  # Keep YAML clean and front-matter friendly
  yaml = hash.to_yaml
  yaml.sub(/\A---\s*\n/, "") # we'll add our own '---'
end

def local_path_from_site_path(site_path)
  return nil unless site_path.is_a?(String)
  p = site_path.strip
  p = p[1..] if p.start_with?("/") # "/assets/..." -> "assets/..."
  p
end

def run_cmd(*cmd)
  stdout, stderr, status = Open3.capture3(*cmd)
  [stdout, stderr, status.success?]
end

def imagemagick_present?
  _, _, ok1 = run_cmd("montage", "-version")
  _, _, ok2 = run_cmd("convert", "-version")
  ok1 && ok2
end

unless Dir.exist?(VISUAL_STORIES_DIR)
  warn "No #{VISUAL_STORIES_DIR}/ directory found. Nothing to do."
  exit 0
end

unless imagemagick_present?
  warn "ImageMagick not found (need 'montage' and 'convert')."
  exit 1
end

FileUtils.mkdir_p(OUTPUT_DIR)

changed_files = 0
generated_images = 0

Dir.glob(File.join(VISUAL_STORIES_DIR, "*.{md,markdown}")).sort.each do |story_path|
  text = File.read(story_path, mode: "r:bom|utf-8")
  fm_str, body = split_front_matter(text)
  next unless fm_str # skip non-front-matter files

  fm = load_yaml(fm_str, story_path)
  panels = fm["panels"]
  hero = fm["hero"]

  # Prefer panels; fallback to hero only if panels missing/empty
  image_sources =
    if panels.is_a?(Array) && !panels.empty?
      panels.map { |p| p.is_a?(Hash) ? p["img"] : nil }.compact
    elsif hero.is_a?(String) && !hero.strip.empty?
      [hero]
    else
      []
    end

  next if image_sources.empty?

  # Resolve local file paths and keep only existing files
  local_images = image_sources.map { |p| local_path_from_site_path(p) }.compact
  local_images.select! { |p| File.exist?(p) }

  # Need at least 1 image to generate a preview
  next if local_images.empty?

  local_images = local_images.first(MAX_PANELS)

  slug = File.basename(story_path).sub(/\.(md|markdown)\z/i, "")
  out_rel = "/#{OUTPUT_DIR}/#{slug}.jpg"
  out_fs  = File.join(OUTPUT_DIR, "#{slug}.jpg")

  # Skip regeneration if output exists and is newer than all inputs
  if File.exist?(out_fs)
    out_mtime = File.mtime(out_fs)
    newest_in = local_images.map { |p| File.mtime(p) }.max
    # also regenerate if the story file itself is newer (panels changed but images same)
    story_mtime = File.mtime(story_path)
    if out_mtime >= newest_in && out_mtime >= story_mtime
      # Still ensure front matter has image set correctly
      if fm["image"] != out_rel
        fm["image"] = out_rel
        new_text = +"---\n#{dump_yaml(fm)}---\n#{body}"
        File.write(story_path, new_text)
        changed_files += 1
      end
      next
    end
  end

  # Build contact sheet:
  # 1) montage images into a grid
  # 2) convert to 1200x630 cover crop, strip metadata, compress
  tile_rows = ((local_images.length.to_f / TILE_COLS).ceil)
  tile = "#{TILE_COLS}x#{tile_rows}"

  tmp = File.join(OUTPUT_DIR, ".tmp_#{slug}.jpg")

  montage_cmd = [
    "montage",
    *local_images,
    "-background", "white",
    "-alpha", "remove",
    "-alpha", "off",
    "-tile", tile,
    "-geometry", "+0+0",
    tmp
  ]

  _, montage_err, ok = run_cmd(*montage_cmd)
  unless ok
    warn "montage failed for #{story_path}:\n#{montage_err}"
    next
  end

  convert_cmd = [
    "convert", tmp,
    "-resize", "#{OUT_W}x#{OUT_H}^",
    "-gravity", "center",
    "-extent", "#{OUT_W}x#{OUT_H}",
    "-strip",
    "-interlace", "Plane",
    "-quality", QUALITY.to_s,
    out_fs
  ]

  _, convert_err, ok2 = run_cmd(*convert_cmd)
  FileUtils.rm_f(tmp)

  unless ok2
    warn "convert failed for #{story_path}:\n#{convert_err}"
    next
  end

  generated_images += 1

  # Update front matter
  if fm["image"] != out_rel
    fm["image"] = out_rel
    new_text = +"---\n#{dump_yaml(fm)}---\n#{body}"
    File.write(story_path, new_text)
    changed_file_
