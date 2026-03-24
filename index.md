---
layout: default
title: "JKD Wednesday Night Group"
subtitle: "Preserve · Promote · Practice"
header_type: none
include_on_search: false
---

<div id="jkd-carousel-wrapper">
<div id="jkd-carousel" class="carousel slide carousel-fade" data-ride="carousel" data-interval="4500">

<ol class="carousel-indicators">
  <li data-target="#jkd-carousel" data-slide-to="0" class="active"></li>
  <li data-target="#jkd-carousel" data-slide-to="1"></li>
  <li data-target="#jkd-carousel" data-slide-to="2"></li>
  <li data-target="#jkd-carousel" data-slide-to="3"></li>
  <li data-target="#jkd-carousel" data-slide-to="4"></li>
  <li data-target="#jkd-carousel" data-slide-to="5"></li>
  <li data-target="#jkd-carousel" data-slide-to="6"></li>
</ol>

<div class="carousel-inner">

<div class="carousel-item active jkd-slide" style="background-image: url('/wp-content/uploads/2023/09/jeet-kune-do-ft.jpg')">
  <div class="carousel-caption">
    <a href="/jeet-kune-do/" class="btn btn-outline-light btn-lg">JEET KUNE DO</a>
  </div>
</div>

<div class="carousel-item jkd-slide" style="background-image: url('/wp-content/uploads/2023/08/gallery.jpg')">
  <div class="carousel-caption">
    <a href="/gallery/" class="btn btn-outline-light btn-lg">GALLERY</a>
  </div>
</div>

<div class="carousel-item jkd-slide" style="background-image: url('/wp-content/uploads/2023/08/instructor-blog-featured.jpg')">
  <div class="carousel-caption">
    <a href="/official/" class="btn btn-outline-light btn-lg">INSTRUCTORS</a>
  </div>
</div>

<div class="carousel-item jkd-slide" style="background-image: url('/wp-content/uploads/2023/08/articles-featured.jpg')">
  <div class="carousel-caption">
    <a href="/blog/" class="btn btn-outline-light btn-lg">JKD BLOG</a>
  </div>
</div>

<div class="carousel-item jkd-slide" style="background-image: url('/wp-content/uploads/2023/10/video-featured.jpg')">
  <div class="carousel-caption">
    <a href="/videos/" class="btn btn-outline-light btn-lg">VIDEOS</a>
  </div>
</div>

<div class="carousel-item jkd-slide" style="background-image: url('/wp-content/uploads/2023/07/articles.jpg')">
  <div class="carousel-caption">
    <a href="/articles/" class="btn btn-outline-light btn-lg">ARTICLES</a>
  </div>
</div>

<div class="carousel-item jkd-slide" style="background-image: url('/wp-content/uploads/2023/08/seminars-featured1.jpg')">
  <div class="carousel-caption">
    <a href="/seminars/" class="btn btn-outline-light btn-lg">SEMINARS</a>
  </div>
</div>

</div>

<a class="carousel-control-prev" href="#jkd-carousel" role="button" data-slide="prev">
  <span class="carousel-control-prev-icon" aria-hidden="true"></span>
  <span class="sr-only">Previous</span>
</a>
<a class="carousel-control-next" href="#jkd-carousel" role="button" data-slide="next">
  <span class="carousel-control-next-icon" aria-hidden="true"></span>
  <span class="sr-only">Next</span>
</a>

</div>
</div>

<div class="container py-4">

<div class="row justify-content-center mb-5">
<div class="col-md-8 text-center">

The purpose of this group is to preserve and promote Bruce Lee's art of Jeet Kune Do, to help define and teach the core curriculum, not to confine us but to liberate us, and to discover our personal expression of Bruce's art.

<a href="/contact/" class="btn btn-primary mt-3">Get In Touch</a>

</div>
</div>

<h2>Training</h2>

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

<h2>Recent Articles</h2>

{% assign articles = site.posts | where_exp: "post", "post.categories contains 'Articles'" %}
<ul>
{% for post in articles limit:5 %}
<li><a href="{{ post.url | relative_url }}">{{ post.title }}</a> — {{ post.date | date: "%B %-d, %Y" }}</li>
{% endfor %}
</ul>

<a href="/articles/">View all articles →</a>

<h2>Recent News &amp; Events</h2>

{% assign events = site.posts | where_exp: "post", "post.categories contains 'Events'" %}
<ul>
{% for post in events limit:3 %}
<li><a href="{{ post.url | relative_url }}">{{ post.title }}</a> — {{ post.date | date: "%B %-d, %Y" }}</li>
{% endfor %}
</ul>

<a href="/blog/">View all posts →</a>

</div>
