---
layout: default
title: "JKD Wednesday Night Group"
subtitle: "Preserve · Promote · Practice"
header_type: hero
image: /wp-content/uploads/2023/08/history-featured.jpg
include_on_search: false
---

<div class="container py-4">

<div class="row justify-content-center mb-5">
<div class="col-md-8 text-center">

The purpose of this group is to preserve and promote Bruce Lee's art of Jeet Kune Do, to help define and teach the core curriculum.

<a href="/contact/" class="btn btn-primary mt-3">Get In Touch</a>

</div>
</div>

## Training

<div class="row mb-5">
<div class="col-md-4 mb-3">
<div class="card h-100">
<div class="card-body">
<h4 class="card-title">Old School JKD</h4>
<p class="card-text">Bruce Lee's Jeet Kune Do as taught through the L.A. Chinatown lineage — direct, efficient, and effective.</p>
<a href="/jeet-kune-do/" class="btn btn-outline-primary btn-sm">Learn More</a>
</div>
</div>
</div>
<div class="col-md-4 mb-3">
<div class="card h-100">
<div class="card-body">
<h4 class="card-title">Combatives</h4>
<p class="card-text">Practical self-defence skills drawn from JKD principles, adapted for real-world application.</p>
<a href="/combatives/" class="btn btn-outline-primary btn-sm">Learn More</a>
</div>
</div>
</div>
<div class="col-md-4 mb-3">
<div class="card h-100">
<div class="card-body">
<h4 class="card-title">Impact &amp; Edged Weapons</h4>
<p class="card-text">Training with impact tools and edged weapons as an extension of the JKD curriculum.</p>
<a href="/impact-edge/" class="btn btn-outline-primary btn-sm">Learn More</a>
</div>
</div>
</div>
</div>

## Recent Articles

{% assign articles = site.posts | where_exp: "post", "post.categories contains 'Articles'" %}
{% for post in articles limit:5 %}
- [{{ post.title }}]({{ post.url | relative_url }}) — {{ post.date | date: "%B %-d, %Y" }}
{% endfor %}

[View all articles →](/articles/)

## Recent News &amp; Events

{% assign events = site.posts | where_exp: "post", "post.categories contains 'Events'" %}
{% for post in events limit:3 %}
- [{{ post.title }}]({{ post.url | relative_url }}) — {{ post.date | date: "%B %-d, %Y" }}
{% endfor %}

[View all posts →](/blog/)

</div>