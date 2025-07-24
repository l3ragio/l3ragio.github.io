require 'net/http'
require 'json'
require 'jekyll'

Jekyll::Hooks.register :site, :pre_render do |site|
  # Replace with your Medium @username
  url = URI("https://medium.com/@your_username?format=json")
  body = Net::HTTP.get(url).sub(/^while\(1\);/, '')  # remove Medium prefix
  js = JSON.parse(body)

  # Grab your bio and avatar
  user = js.dig("payload", "user")
  about = {
    "name" => user["name"],
    "bio"  => user["bio"],
    "image" => user["imageId"]
  }

  # Save as a data file accessible in Liquid
  File.write(File.join(site.source, "_data", "medium_about.json"), JSON.generate(about))
end
