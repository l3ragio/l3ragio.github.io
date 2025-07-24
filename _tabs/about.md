---
layout: page
title: About
---

{% assign about = site.data.medium_about %}
{% if about and about.name %}
## About {{ about.name }}

{% if about.avatar_url %}
![{{ about.name }}]({{ about.avatar_url }})
{% endif %}

{{ about.bio }}

Find me on [Medium](https://medium.com/@{{ about.username }})
{% else %}
No profile data yet. Make sure `medium_username` is set in `_config.yml`.
{% endif %}
