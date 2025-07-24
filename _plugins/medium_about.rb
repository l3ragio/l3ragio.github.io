# _plugins/medium_about.rb
require 'open-uri'
require 'json'
require 'jekyll'

Jekyll::Hooks.register :site, :post_read do |site|
  username = site.config['medium_username']
  url = "https://medium.com/@#{username}/about?format=json"
  raw = URI.open(url).read
  clean = raw.gsub(/\A\)\]\}while\(1\);\s*<x>/, '')
  data = JSON.parse(clean)

  user = data.dig('payload', 'user') || {}
  about_html = user['aboutMe'] || user['bio'] || ''

  site.data['medium_about'] = {
    'name'        => user['name'],
    'username'    => username,
    'avatar_url'  => user['imageId'] ? "https://cdn-images-1.medium.com/fit/c/200/200/#{user['imageId']}" : nil
  }
  site.data['medium_about_html'] = about_html
end
