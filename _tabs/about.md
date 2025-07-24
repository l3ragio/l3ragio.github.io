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

---

{% endif %}

<!-- Begin manual content from Medium About page -->

<img src="https://miro.medium.com/v2/resize:fit:1313/1*u2rbaO2KNkYlWddDuhFAQA.jpeg" alt="About Hero Image" width="100%" />

**Beyond my practical work, my passion for cybersecurity has led me to explore the academic sphere.**

One of my most remarkable academic experiences was being invited by Prof. Dr. Cas Cremers at CISPA to deliver a talk titled **“Questioning the Oracle.”**  
This provided an excellent platform to present my work on breaking security properties against Compression Functions, a key building block of hash functions and PRNGs.

My explorations into Quantum circuits as a potential solution to avoid the risk of arithmetic-circuit analysis further signify my creative approach to tackling complex cybersecurity problems.

As I continue to grow in my career, I stay connected with the broader cybersecurity community through my Medium blog, where I discuss and analyze emerging concepts, techniques, and scenarios related to prominent threats and promising technologies.

My commitment to continuous learning, coupled with my diverse experiences, fuels my desire to contribute meaningful insights and solutions to the field of cybersecurity.

*Stay tuned for more discussions and discoveries in the ever-evolving world of cybersecurity!*
