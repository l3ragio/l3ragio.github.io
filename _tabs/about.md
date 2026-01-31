---
layout: page
title: About
---

{% assign about = site.data.medium_about %}
{% if about and about.name %}
### {{ about.name }}

{% if about.avatar_url %}
![{{ about.name }}]({{ about.avatar_url }})
{% endif %}

{{ about.bio }}

Find me on [Medium](https://medium.com/@{{ about.username }})

---

{% endif %}

<!-- Begin manual content from Medium About page -->

<img src="https://miro.medium.com/v2/resize:fit:1313/1*u2rbaO2KNkYlWddDuhFAQA.jpeg" alt="About Hero Image" width="100%" />

Davide Bragetti is an independent AI researcher, frontier Red Team leader and operator, and trusted adviser in regulated-industry settings. With dual PhDs in cybersecurity, his career spans collaborations with companies such as Anthropic, Microsoft, Google, Tesla, Meta and Apple, and work with the European Commission, the European Central Bank and the United Nations—alongside leading global universities and research centers.


He now supports organizations in building resilient, auditable AI systems—guiding assurance frameworks, telemetry and adversarial testing of models and platforms—while advancing scientific insight into how AI models behave and fail. He is committed to embedding governance, adversary-aware monitoring and adaptive assurance into mission-critical deployments, enabling organisations to stay ahead in a world where intelligent systems and sophisticated adversaries evolve together.
