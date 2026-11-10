# frozen_string_literal: true
#
# Give pages and non-post documents a real last-modified date for the sitemap.
#
# jekyll-sitemap falls back to the file's mtime, which on CI is the checkout
# time, so every deploy would stamp every such URL as "changed now". Here the
# date is the last commit that touched the source file (and, optionally, files
# the page is rendered from, listed in front matter as `lastmod_deps`).
#
# - An explicit `last_modified_at` in front matter wins (the generated
#   _papers/*.md carry one, moved only by a real content change).
# - Posts are left to _plugins/posts-lastmod-hook.rb, because the theme's
#   "Recently Updated" panel reads the same field.
# - Needs git history (CI checks out with fetch-depth: 0). Without it, or for
#   an uncommitted file, nothing is set and Jekyll's default applies.

module PagesLastmod
  def self.commit_date(paths)
    out = IO.popen(["git", "log", "-1", "--format=%aI", "--", *paths], err: File::NULL, &:read)
    out.to_s.strip
  rescue StandardError
    ""
  end
end

Jekyll::Hooks.register [:pages, :documents], :post_init do |item|
  next if item.respond_to?(:collection) && item.collection&.label == "posts"
  next if item.data["last_modified_at"]

  paths = [item.path] + Array(item.data["lastmod_deps"])
  date = PagesLastmod.commit_date(paths)
  item.data["last_modified_at"] = date unless date.empty?
end
