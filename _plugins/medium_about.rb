# _plugins/medium_about.rb
require 'open-uri'
require 'nokogiri'
require 'jekyll'

Jekyll::Hooks.register :site, :post_read do |site|
  username = site.config['medium_username']
  about_url = "https://medium.com/@#{username}/about?format=json"
  raw = URI.open(about_url).read
  clean = raw.sub(/\A\]\)\}while\(1\);<\/x>/, '')
  json = JSON.parse(clean)
  html = json.dig('payload','value','content','bodyModel','paragraphs')
  # Sometimes Medium's structure differs - handle exceptions
  html ||= json.dig('payload','user','about') || ''

  # If we got an array of paragraphs, reconstruct HTML
  if html.is_a?(Array)
    doc = Nokogiri::HTML::DocumentFragment.parse('')
    html.each do |p|
      # those paragraphs contain text, markup or image data
      fragment = Nokogiri::HTML::DocumentFragment.parse(p['text'] || '')
      doc.add_child(fragment)
    end
    about_html = doc.to_html
  else
    about_html = html
  end

  site.data['medium_about_html'] = about_html
end
