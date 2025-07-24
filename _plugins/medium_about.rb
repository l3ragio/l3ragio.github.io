# _plugins/medium_about.rb
require 'open-uri'
require 'jekyll'

Jekyll::Hooks.register :site, :post_read do |site|
  username = site.config['medium_username']
  url      = "https://medium.com/@#{username}/about?format=json"
  raw      = URI.open(url).read
  clean    = raw.sub(/\A\]\)\}while\(1\);<\/x>/, '')
  data = JSON.parse(clean)

  content_html = data.dig('payload','value')&.[]('content') || ''
  name = data.dig('payload','user','name') || username
  imgid = data.dig('payload','user','imageId')

  site.data['medium_about'] = {
    'name'        => name,
    'username'    => username,
    'avatar_url'  => "https://cdn-images-1.medium.com/fit/c/200/200/#{imgid}",
    'html'        => content_html
  }
end
