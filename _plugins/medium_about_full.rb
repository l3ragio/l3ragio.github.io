# _plugins/medium_about_full.rb
require 'open-uri'
require 'json'
require 'jekyll'

Jekyll::Hooks.register :site, :post_read do |site|
  username = site.config['medium_username']
  # Query Medium GraphQL endpoint for about content
  body = {
    operationName: "UserProfileAboutQuery",
    variables: { username: username },
    query: <<~GRAPHQL
      query UserProfileAboutQuery($username: String!) {
        user(username: $username) {
          about {
            html
          }
        }
      }
    GRAPHQL
  }.to_json

  response = URI.open("https://medium.com/_/graphql", "Content-Type" => "application/json", &:read)
  clean = response.sub(/\A\)\]\}'/, '')
  data = JSON.parse(clean)
  about_html = data.dig("data", "user", "about", "html") || ""

  site.data["medium_about_full"] = about_html
end
