# frozen_string_literal: true
#
# Scholarly paper pages (collection `papers`): page date and page author for
# jekyll-seo-tag, which describes each landing page as a WebPage (see the
# `papers` defaults in _config.yml).
#
# - Date. The generated _papers/*.md carry `publication_date` but no `date`, so
#   Jekyll dated them with the build time, and jekyll-seo-tag published that
#   build time as datePublished and article:published_time: it changed on every
#   deploy and contradicted the ScholarlyArticle JSON-LD and
#   citation_publication_date, both taken from `publication_date`. `date` is
#   now `publication_date`.
# - Author. Without an explicit `author`, jekyll-seo-tag took the first entry of
#   the Highwire `authors` list ("Family, Given") as the author of the page. The
#   landing page is maintained by the site owner (site `author`); the paper's
#   full author list stays in the ScholarlyArticle JSON-LD and the
#   citation_author tags, which read `authors`, not `author`.
#
# Neither field is read by _includes/paper-meta.html or _layouts/paper.html, and
# the sitemap lastmod keeps using `last_modified_at`.

Jekyll::Hooks.register :site, :post_read do |site|
  papers = site.collections["papers"]
  next unless papers

  owner = site.config["author"]
  papers.docs.each do |doc|
    pub = doc.data["publication_date"]
    unless pub.nil? || pub.to_s.strip.empty?
      doc.data["date"] = Jekyll::Utils.parse_date(pub.to_s, "Invalid publication_date in #{doc.relative_path}")
    end
    doc.data["author"] ||= owner if owner
  end
end
