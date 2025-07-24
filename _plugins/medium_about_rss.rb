require 'feedjira'
require 'jekyll'

Jekyll::Hooks.register :site, :post_read do |site|
  username = site.config['medium_username']
  feed_url = "https://medium.com/feed/@#{username}"
  
  feed = Feedjira.parse(URI.open(feed_url).read)
  about_entry = feed.entries.find { |e| e.url.include?('/about') }

  if about_entry
    site.data['medium_about'] = {
      'title' => about_entry.title,
      'content' => about_entry.content
    }
  else
    Jekyll.logger.warn "MediumAbout:", "Couldn't find /about in RSS feed."
  end
end
