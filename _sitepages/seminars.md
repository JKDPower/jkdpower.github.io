---
title: 'Jeet Kune Do Seminars'
layout: page
image: /wp-content/uploads/2023/08/seminars-featured1.jpg
header_type: hero
permalink: /seminars/
include_on_search: true
show_author: false
---

[Dennis Blue](/dennis/), [Jeremy Lynch](/jeremy/), [Vince Raimondi](/vince/) and most of the JKD Wednesday Night Group [Instructors](/official/) are available to conduct seminars at your school.

For seminar inquiries, contact us at <contact@jkdwednite.com>.

---

## Upcoming & Recent Seminars

{% assign seminars = site.posts | where_exp: "post", "post.categories contains 'Events'" %}
{% for post in seminars limit:10 %}
### [{{ post.title }}]({{ post.url | relative_url }})

{{ post.date | date: "%B %-d, %Y" }}

{% if post.excerpt %}{{ post.excerpt | strip_html | truncatewords: 40 }}{% endif %}

---
{% endfor %}
