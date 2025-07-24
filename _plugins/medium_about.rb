# _plugins/medium_about.rb
require 'open-uri'
require 'nokogiri'

Jekyll::Hooks.register :site, :post_read do |site|
  username = site.config['medium_username']
  url = "https://medium.com/@#{username}/about"
  html = URI.open(url).read

  doc = Nokogiri::HTML(html)

  # Select the actual rendered content in the <article> tag
  article = doc.at('article')

  if article
    # Clean up unwanted scripts or attributes if needed
    article.search('script, style, noscript').remove
    site.data['medium_about_html'] = article.inner_html
  else
    site.data['medium_about_html'] = "<p>Unable to fetch Medium About content.</p>"
  end
end
