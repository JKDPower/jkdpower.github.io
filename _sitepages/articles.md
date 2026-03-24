---
title: 'Jeet Kune Do Articles'
date: '2023-07-18T05:27:13+00:00'
author: 'JKD WNG'
layout: default
header_type: hero
image: /wp-content/uploads/2023/08/articles-featured.jpg
permalink: /articles/
---



Articles written by JKD Wednesday Night Group [Instructors](/official/) that have been featured in Black Belt Magazine, Budo International, Masters Magazine, Martial Arts Illustrated, and other current and historical publications. Also, be sure to check out our [Jeet Kune Do](/blog/) and [Combatives](/self-defense-blog/) blogs for the most recent posts.

{% assign articles = site.posts | where_exp: "post", "post.categories contains 'Articles'" | sort: "date" | reverse %}

<div class="row mt-4">
{% for post in articles %}
<div class="col-12 mb-4">
  <div class="card h-100 border-0 shadow-sm">
    <div class="row g-0">
      {% if post.image %}<a href="{{ post.url | relative_url }}" class="col-sm-3 d-none d-sm-flex" style="background-image: url('{{ post.image }}'); background-size: cover; background-position: center; min-height: 140px;"></a>{% endif %}
      <div class="col">
        <div class="card-body">
          <h5 class="card-title mb-1"><a href="{{ post.url | relative_url }}" class="text-decoration-none">{{ post.title }}</a></h5>
          <p class="text-muted small mb-2">{{ post.author }}{% if post.date %} &mdash; {{ post.date | date: "%B %-d, %Y" }}{% endif %}</p>
          <p class="card-text">{{ post.excerpt | strip_html | truncatewords: 35 }}</p>
          <a href="{{ post.url | relative_url }}" class="btn btn-outline-primary btn-sm">Read More</a>
        </div>
      </div>
    </div>
  </div>
</div>
{% endfor %}
</div>