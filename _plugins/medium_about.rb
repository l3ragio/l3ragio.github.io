# Place in `_plugins/medium_about.rb`

require 'net/http'
require 'json'

Jekyll::Hooks.register :site, :pre_render do |site|
  medium_url = "https://medium.com/@YOUR_MEDIUM_USERNAME"
  uri = URI("#{medium_url}/?format=json")
  data = JSON.parse(Net::HTTP.get(uri).sub('])}while(1);</x>', ''))
  site.config['medium_about'] = {
    "name" => data["payload"]["user"]["name"],
    "bio"  => data["payload"]["user"]["bio"],
    "avatar" => data["payload"]["user"]["imageId"], # may require build URL
  }
end
