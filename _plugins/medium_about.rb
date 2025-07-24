require 'open-uri'
require 'json'
require 'jekyll'

Jekyll::Hooks.register :site, :post_read do |site|
  username = site.config['medium_username']
  url      = "https://medium.com/@#{username}?format=json"
  raw      = URI.open(url).read
  clean    = raw.sub(/\A\]\)\}while\(1\);<\/x>/, '')
  data     = JSON.parse(clean)

  profile = data.dig('payload', 'user') || {}
  site.data['medium_about'] = {
    'name'       => profile['name'],
    'username'   => username,
    'bio'        => (profile['bio'] || profile['description'] || ''),
    'avatar_url' => "https://cdn-images-1.medium.com/fit/c/200/200/#{profile['imageId']}"
  }
end
