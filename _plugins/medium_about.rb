# _plugins/medium_about.rb
require 'open-uri'
require 'nokogiri'
require 'jekyll'

Jekyll::Hooks.register :site, :post_read do |site|
  username = site.config['medium_username']
  about_url = "https://medium.com/@#{username}/about?format=json"
  raw = URI.open(about_url).read
  json = raw.sub(/\A\]\)\}while\(1\);<\/x>/, '')
  payload = JSON.parse(json)['payload']
  
  # Fetch the “about” HTML content
  about_json = payload.dig('user', 'aboutModel') || {}
  about_content = about_json['subtitle'] || about_json['about'] || ''

  # Clean HTML to allow necessary tags & strip scripts
  doc = Nokogiri::HTML::DocumentFragment.parse(about_content)
  allowed = %w[p img a strong em ul ol li br blockquote h2 h3 h4 figure figcaption]
  doc.css('*').each do |node|
    node.remove unless allowed.include?(node.name)
    node['href']&.gsub!(/^\/\//, 'https://')
  end

  site.data['medium_about_full'] = {
    'html' => doc.to_html,
    'name' => payload.dig('user', 'name') || '',
    'avatar_url' => payload.dig('user', 'imageId') ? "https://cdn-images-1.medium.com/fit/c/200/200/#{payload['user']['imageId']}" : ''
  }
end
