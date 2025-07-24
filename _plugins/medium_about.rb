# _plugins/medium_about.rb
require 'open-uri'
require 'json'
require 'jekyll'

Jekyll::Hooks.register :site, :post_read do |site|
  username = site.config['medium_username']
  return unless username && !username.empty?

  url = "https://medium.com/@#{username}?format=json"
  begin
    raw = URI.open(url).read
    clean = raw.sub(/\A\]\)\}while\(1\);<\/x>/, '')
    data = JSON.parse(clean)

    profile = data.dig('payload', 'user')
    raise unless profile

    site.data['medium_about'] = {
      'name'        => profile['name'] || '',
      'username'    => username,
      'bio'         => (profile['bio'] || profile['description'] || ''),
      'avatar_url'  => profile['imageId'] ? "https://cdn-images-1.medium.com/fit/c/200/200/#{profile['imageId']}" : ''
    }
  rescue => e
    Jekyll.logger.warn "MediumAbout:", "Failed to fetch Medium profile for @#{username}: #{e.message}"
    site.data['medium_about'] ||= {}
  end
end
