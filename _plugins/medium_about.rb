# _plugins/medium_about.rb
require 'open-uri'
require 'nokogiri'
require 'jekyll'

Jekyll::Hooks.register :site, :post_read do |site|
  username = site.config['medium_username']
  about_url = "https://medium.com/@#{username}/about"

  begin
    doc = Nokogiri::HTML(URI.open(about_url))
    article = doc.at_css('article') || doc.at_css('main') || doc.at_css('.u-marginTop20')
    html = article ? article.inner_html.strip : "<p>Error: couldn't locate 'about' content.</p>"

    site.data['medium_about_html'] = html
  rescue => e
    site.data['medium_about_html'] = "<p>Unable to fetch Medium About content.</p>"
    Jekyll.logger.error "medium_about:", "Error reading Medium about: #{e.message}"
  end
end
