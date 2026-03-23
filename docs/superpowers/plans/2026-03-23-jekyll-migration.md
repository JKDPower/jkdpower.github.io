# Jekyll Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Migrate a WordPress export to a fully working Jekyll site using the Chulapa remote theme, with correct routing, clean content, and a homepage modelled on the original jkdwednite.com.

**Architecture:** The `_pages/` directory is renamed to `_sitepages/` and declared as a Jekyll collection named `sitepages`. Every page gets an explicit `permalink:` in its frontmatter. WordPress SiteOrigin HTML is rewritten to clean Markdown. A Python script handles batch frontmatter cleanup across pages and posts.

**Tech Stack:** Jekyll 4.4, Ruby/Bundler, Chulapa remote theme (dieghernan/chulapa), Bootstrap 4 (via Chulapa), Python 3.12 (for batch scripts), GitHub Pages

**Reference spec:** `docs/superpowers/specs/2026-03-23-jekyll-migration-design.md`
**Original site:** https://jkdwednite.com/ (live reference for content)

---

## Files Overview

| Action | File | Purpose |
|--------|------|---------|
| Modify | `_config.yml` | Site config: title, nav, collections, defaults |
| Rename | `_pages/` → `_sitepages/` | Jekyll collection directory |
| Replace | `index.md` | New homepage |
| Delete | `_sitepages/blog.md` | Collides with `blog/index.html` |
| Delete | `_sitepages/home-page.md` | Replaced by `index.md` |
| Delete | `_sitepages/cheatsheet.md` | Cheatsheet feature removed |
| Delete | `_sitepages/current_skin.md` | Demo page |
| Delete | `_posts/2025-10-03-landing-page.md` | Demo post |
| Delete | `_posts/2025-10-13-current-skin.md` | Demo post |
| Delete | `_cheatsheet/` | Cheatsheet collection removed |
| Modify | `_sitepages/404.md` | Add `include_on_search: false` |
| Rewrite | `_sitepages/members.md` | SiteOrigin → clean Markdown photo grid |
| Rewrite | `_sitepages/seminars.md` | SiteOrigin blog widget → clean Markdown |
| Rewrite | `_sitepages/official.md` | SiteOrigin → clean instructor list |
| Modify | 13 simple pages | Strip WP frontmatter, add permalink, fix links |
| Modify | 17 instructor pages | Strip WP frontmatter, add permalink, fix images |
| Modify | 46 posts | Strip WP frontmatter, normalize author field |

---

## Task 1: Update `_config.yml`

**Files:**
- Modify: `_config.yml`

- [ ] **Step 1: Replace `_config.yml` with the new content below**

Replace the entire file with:

```yaml
github: [metadata]

remote_theme: dieghernan/chulapa

# A. Site Settings
locale                  :
title                   : JKD Wednesday Night Group
title_separator         :
subtitle                : Preserving and promoting Bruce Lee's art of Jeet Kune Do
description             : The Wednesday Night Group preserves and promotes Bruce Lee's art of Jeet Kune Do.
url                     :
baseurl                 :
repository              : jkdpower/jkdpower.github.io
words_per_minute        :
timezone                : America/Los_Angeles

# SEO
og_image                :
twitter_site            :
author:
  name                  : JKD Wednesday Night Group
  avatar                :
  location              : "Redlands, California"

fa_version              :
fa_kit_code             :
fa_v4_support           :

gtag_id                 :
analytics_id            :

# Search
search:
  provider              : fusejs
  label                 :
  landing_page          :
  maxwords              :
  show_attrib           :

comments:
  provider              :
  disqus_shortname      :

# B. Navigation
navbar:
  style     :
  expand    :
  brand:
    title   : Home
    url     : /
    img     :
  nav:
  - title   : About
    url     : /about/
  - title   : Training
    child   :
      - title : Jeet Kune Do
        url   : /jeet-kune-do/
      - title : Combatives
        url   : /combatives/
      - title : Seminars
        url   : /seminars/
      - title : Classes
        url   : /classes/
  - title   : Media
    child   :
      - title : Articles
        url   : /articles/
      - title : Blog
        url   : /blog/
      - title : Videos
        url   : /videos/
      - title : Gallery
        url   : /gallery/
      - title : Books
        url   : /books/
  - title   : Members
    url     : /members/
  - title   : Contact
    url     : /contact/

footer:
  links:
    - label : Facebook
      icon  : fab fa-facebook
      url   : https://www.facebook.com/jkdwednite  # TODO: verify URL from original site footer
    - label : Instagram
      icon  : fab fa-instagram
      url   : https://www.instagram.com/jkdwednite  # TODO: verify URL from original site footer
    - label : YouTube
      icon  : fab fa-youtube
      url   : https://www.youtube.com/@jkdwednite  # TODO: verify URL from original site footer
    - label : RSS
      icon  : fa fa-rss
      url   : ./atom.xml
  copyright : "© JKD Wednesday Night Group"

# C. Theme Settings
googlefonts:

chulapa-skin:
  highlight     :
  skin          :
  autothemer    : true
  vars          :
    primary     : "lightskyblue"

# D. Jekyll Defaults and Collections
paginate      : 4
paginate_path : "/blog/page:num/"
paginator_maxnum : 3

collections:
  sitepages:
    output    : true
    permalink : /:name/

collections_dir :
permalink       : /:year:month:day_:title/

defaults:
  -
    scope:
      path: ""
    values:
      layout              : "default"
      header_type         : "base"
      include_on_search   : false
      cloudtag_url        : /tags
      cloudcategory_url   : /categories
  -
    scope:
      path: ""
      type: "sitepages"
    values:
      layout              : page
      header_type         : base
      show_author         : false
      include_on_search   : true
  -
    scope:
      path: ""
      type: "posts"
    values:
      header_type         : "post"
      include_on_search   : true
      include_on_feed     : true
      show_date           : true
      show_related        : true
      show_bottomnavs     : true
      show_sociallinks    : true
      show_comments       : true
      show_tags           : true
      show_categories     : true
      show_author         : true
      show_breadcrumb     : true
      breadcrumb_list     :
        - label: Blog
          url: /blog/

# XX. Other settings
compress_html:
  clippings: all
  blanklines: true

plugins:
  - jekyll-github-metadata
  - jekyll-paginate
  - jekyll-include-cache
  - jekyll-sitemap

exclude:
  - LICENSE
  - README.md
  - Gemfile
  - vendor
  - docs/

# Conversion
markdown    : kramdown
highlighter : rouge
lsi         : false
excerpt_separator: "\n\n"
incremental : false

kramdown:
  input           : GFM
  hard_wrap       : false
  auto_ids        : true
  footnote_nr     : 1
  footnote_backlink: '&uarr;'
  entity_output   : as_char
  toc_levels      : 2..6
  smart_quotes    : lsquo,rsquo,ldquo,rdquo
  enable_coderay  : false

sass:
  sass_dir    : _sass
  style       : compressed
  quiet_deps  : true
  silence_deprecations:
    - import
    - global-builtin
    - color-functions
    - mixed-decls
    - function-units
    - abs-percent
```

> **Note on footer social URLs:** Open https://jkdwednite.com/ and check the footer for the exact Facebook, Instagram, and YouTube URLs. Update the three `# TODO` lines above before committing.

- [ ] **Step 2: Commit**

```bash
cd /c/Users/Bitpusher/workspace/jkdpower.github.io
git add _config.yml
git commit -m "feat: update _config.yml for JKD site (nav, collections, identity)"
```

---

## Task 2: Rename `_pages/` → `_sitepages/` and delete demo content

**Files:**
- Rename: `_pages/` → `_sitepages/`
- Delete: several files (see steps)

> **Critical:** Do this in a single commit with the config change so Jekyll never tries to build with `include: _pages` pointing at a missing directory.

- [ ] **Step 1: Rename the directory**

```bash
cd /c/Users/Bitpusher/workspace/jkdpower.github.io
git mv _pages _sitepages
```

- [ ] **Step 2: Delete demo and redundant files**

```bash
git rm _sitepages/blog.md
git rm _sitepages/home-page.md
git rm _sitepages/cheatsheet.md
git rm _sitepages/current_skin.md
git rm _posts/2025-10-03-landing-page.md
git rm _posts/2025-10-13-current-skin.md
git rm _cheatsheet/01_markdown-cheat-sheet.md
git rm _cheatsheet/02_kramdown-cheat-sheet.md
```

- [ ] **Step 3: Commit**

```bash
git add -A
git commit -m "feat: rename _pages to _sitepages, delete Chulapa demo content"
```

---

## Task 3: Verify baseline build

**Files:** None — verification only.

- [ ] **Step 1: Build the site**

```bash
cd /c/Users/Bitpusher/workspace/jkdpower.github.io
bundle exec jekyll build --strict_front_matter 2>&1 | tail -40
```

Expected: Build completes without errors. It's OK to see warnings about missing layout `page` for any remaining SiteOrigin pages.

- [ ] **Step 2: Spot-check output paths**

```bash
ls _site/about/ _site/contact/ _site/members/ 2>&1
```

Expected: Each directory exists with an `index.html` inside.

- [ ] **Step 3: Check blog pagination still works**

```bash
ls _site/blog/
```

Expected: `index.html` present (and `page2/`, `page3/` etc. if enough posts).

> If the build fails, check the error message carefully. Common causes:
> - YAML parse error in a frontmatter field (the serialized SiteOrigin data can confuse Jekyll)
> - Missing layout reference
> Fix the specific file mentioned in the error before proceeding.

---

## Task 4: Build new homepage (`index.md`)

**Files:**
- Modify: `index.md`

- [ ] **Step 1: Replace `index.md` with the new homepage**

```markdown
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
```

- [ ] **Step 2: Build and verify**

```bash
bundle exec jekyll build --strict_front_matter 2>&1 | grep -E "error|warn|done" -i
ls _site/index.html
```

Expected: `_site/index.html` exists and build is clean.

- [ ] **Step 3: Commit**

```bash
git add index.md
git commit -m "feat: replace starter homepage with JKD site homepage"
```

---

## Task 5: Fix infrastructure page (404)

**Files:**
- Modify: `_sitepages/404.md`

- [ ] **Step 1: Add `include_on_search: false` to 404.md frontmatter**

Read the current frontmatter of `_sitepages/404.md`, then add one line:

```yaml
include_on_search: false
```

The 404 page already has `permalink: /404.html` in its frontmatter — leave that as-is.

- [ ] **Step 2: Commit**

```bash
git add _sitepages/404.md
git commit -m "fix: exclude 404 page from search index"
```

---

## Task 6: Batch-update simple pages

**Files (13 pages):**
`about.md`, `contact.md`, `jeet-kune-do.md`, `combatives.md`, `impact-edge.md`, `classes.md`, `videos.md`, `articles.md`, `gallery.md`, `books.md`, `group-news.md`, `self-defense-blog.md`, `privacy.md`, `affiliated.md`

Each page needs:
1. WP garbage frontmatter stripped
2. `permalink:` added
3. Internal links rewritten (`https://jkdwednite.com/foo/` → `/foo/`)
4. Image URLs rewritten (`https://i0.wp.com/jkdwednite.com/wp-content/uploads/` → `/wp-content/uploads/`)
5. Key pages: add `header_type: hero`

- [ ] **Step 1: Write the batch cleanup script**

Create `docs/superpowers/tools/clean_pages.py`:

```python
#!/usr/bin/env python3
"""Strip WordPress garbage frontmatter from Jekyll pages and fix internal links."""

import re
import sys
from pathlib import Path

# Fields to remove (including all their indented continuation lines)
REMOVE_FIELDS = [
    'id', 'guid', 'siteorigin_page_settings', 'siteorigin_premium_meta',
    'two_optimized_date', 'two_page_speed', 'ppma_authors_name',
    'ppma_disable_author_box', 'footnotes', 'panels_data',
    'siteorigin_panels_data',
]

def strip_frontmatter_fields(fm_text: str) -> str:
    """Remove unwanted fields from YAML frontmatter text."""
    lines = fm_text.splitlines(keepends=True)
    result = []
    skipping = False
    for line in lines:
        stripped = line.rstrip('\n\r')
        # A top-level YAML key starts at column 0 and contains ':'
        if stripped and not stripped[0].isspace() and ':' in stripped:
            key = stripped.split(':')[0].strip()
            skipping = key in REMOVE_FIELDS
        elif not stripped.strip():
            # Blank line resets skip state
            skipping = False
        if not skipping:
            result.append(line)
    return ''.join(result)

def fix_links(content: str) -> str:
    """Rewrite absolute jkdwednite.com links to relative paths."""
    # Fix image URLs (WordPress image CDN)
    content = re.sub(
        r'https://i\d+\.wp\.com/jkdwednite\.com(/wp-content/uploads/[^)"?\s]+)',
        r'\1',
        content
    )
    # Strip resize/ssl query params from wp.com image URLs
    content = re.sub(
        r'(/wp-content/uploads/[^)"?\s]+)\?[^)">\s]*',
        r'\1',
        content
    )
    # Fix absolute site links
    content = re.sub(
        r'https?://jkdwednite\.com(/[^)">\s]*)',
        r'\1',
        content
    )
    return content

def clean_file(path: Path, permalink: str, header_type: str = None,
               add_author: bool = False) -> None:
    text = path.read_text(encoding='utf-8')

    if not text.startswith('---'):
        print(f'SKIP (no frontmatter): {path}')
        return

    # Split frontmatter from body
    end = text.find('\n---', 3)
    if end == -1:
        print(f'SKIP (no frontmatter end): {path}')
        return

    fm_text = text[4:end]
    body = text[end+4:]

    # Strip garbage fields
    fm_text = strip_frontmatter_fields(fm_text)

    # Add/replace permalink
    fm_text = re.sub(r'^permalink:.*\n', '', fm_text, flags=re.MULTILINE)
    fm_text = fm_text.rstrip() + f'\npermalink: {permalink}\n'

    # Add header_type if specified
    if header_type:
        fm_text = re.sub(r'^header_type:.*\n', '', fm_text, flags=re.MULTILINE)
        fm_text = fm_text.rstrip() + f'\nheader_type: {header_type}\n'

    # Fix links in body
    body = fix_links(body)

    result = '---\n' + fm_text.lstrip() + '---\n' + body
    path.write_text(result, encoding='utf-8')
    print(f'OK: {path}')


if __name__ == '__main__':
    base = Path('/c/Users/Bitpusher/workspace/jkdpower.github.io/_sitepages')

    pages = {
        'about.md':           ('/about/',           'hero'),
        'contact.md':         ('/contact/',          None),
        'jeet-kune-do.md':    ('/jeet-kune-do/',     'hero'),
        'combatives.md':      ('/combatives/',        'hero'),
        'impact-edge.md':     ('/impact-edge/',       None),
        'classes.md':         ('/classes/',           None),
        'videos.md':          ('/videos/',            None),
        'articles.md':        ('/articles/',          None),
        'gallery.md':         ('/gallery/',           None),
        'books.md':           ('/books/',             None),
        'group-news.md':      ('/group-news/',        None),
        'self-defense-blog.md': ('/self-defense-blog/', None),
        'privacy.md':         ('/privacy/',           None),
        'affiliated.md':      ('/affiliated/',        None),
    }

    for filename, (permalink, header_type) in pages.items():
        clean_file(base / filename, permalink, header_type)
```

- [ ] **Step 2: Run the script**

```bash
cd /c/Users/Bitpusher/workspace/jkdpower.github.io
python docs/superpowers/tools/clean_pages.py
```

Expected: One `OK: ...` line per file, no `SKIP` lines.

- [ ] **Step 3: Manual cleanup — WordPress HTML blocks**

Some pages contain inline HTML from WordPress that won't render well. For each of these pages, open the file and clean up the specific elements:

**`jeet-kune-do.md`** — Remove the `<figure class="wp-block-image">` at the top (it duplicates the hero image). Replace the `<div class="nfd-my-0 ...">` CTA block with plain Markdown:

```markdown
## Begin your Jeet Kune Do Training

Connect with a qualified JKD Instructor, book a seminar, or schedule a virtual training session.

[Find a certified JKD Instructor in your area](/official/) | [Contact us to get help finding the right path](/contact/)
```

Remove the `<figure class="wp-block-pullquote">` wrapper — keep the blockquote and cite content as standard Markdown:

```markdown
> "What we want our students to do is to be able to do the core curriculum of Jeet Kune Do, make it his or her own..."
>
> — Tim Tackett
```

**`contact.md`** — Clean. No HTML blocks. Just link fixes (handled by script).

**`about.md`** — Clean. Long text with internal links. Just link fixes.

**`affiliated.md`** — Has `<span style="text-decoration: underline;">` tags. Replace:
```html
**<span style="text-decoration: underline;">United States</span>**
```
with:
```markdown
**United States**
```
(Do this for all `<span style>` tags in the file.)

**Other pages** — Check each page for similar minor HTML artefacts and convert to Markdown equivalents.

- [ ] **Step 4: Build and verify**

```bash
bundle exec jekyll build --strict_front_matter 2>&1 | tail -20
ls _site/about/ _site/contact/ _site/jeet-kune-do/ _site/affiliated/
```

Expected: All directories exist. No build errors.

- [ ] **Step 5: Commit**

```bash
cd /c/Users/Bitpusher/workspace/jkdpower.github.io
git add _sitepages/about.md _sitepages/contact.md _sitepages/jeet-kune-do.md \
        _sitepages/combatives.md _sitepages/impact-edge.md _sitepages/classes.md \
        _sitepages/videos.md _sitepages/articles.md _sitepages/gallery.md \
        _sitepages/books.md _sitepages/group-news.md _sitepages/self-defense-blog.md \
        _sitepages/privacy.md _sitepages/affiliated.md \
        docs/superpowers/tools/clean_pages.py
git commit -m "feat: add permalinks, strip WP frontmatter, fix links in simple pages"
```

---

## Task 7: Rewrite `members.md`

**Files:**
- Modify: `_sitepages/members.md`

The current file contains SiteOrigin widget HTML. Replace the entire body with clean Markdown. The content below is extracted from the existing file; image files exist at the paths shown.

- [ ] **Step 1: Replace `_sitepages/members.md`**

```markdown
---
title: Members
layout: page
image: /wp-content/uploads/2023/08/WNG-red-black.jpg
header_type: hero
permalink: /members/
include_on_search: true
show_author: false
---

The Wednesday Night Group has attracted many interesting individuals over the years. The men recognized here as Founding Members have shaped our approach to JKD and are responsible for the group being what it is today.

## Founding Members

<div class="row">
<div class="col-md-3 col-sm-6 text-center mb-4">
<img src="/wp-content/uploads/2023/07/bob_bremer-2.jpg" alt="Bob Bremer" class="img-fluid rounded mb-2" style="max-height:220px">

**[Bob Bremer](/bob/)**
Trained with Bruce Lee in L.A. Chinatown starting in 1967
</div>
<div class="col-md-3 col-sm-6 text-center mb-4">
<img src="/wp-content/uploads/2023/07/tim_tackett-1.jpg" alt="Tim Tackett" class="img-fluid rounded mb-2" style="max-height:220px">

**[Tim Tackett](/tim/)**
Joined Dan Inosanto's "Backyard" JKD group in 1971
</div>
<div class="col-md-3 col-sm-6 text-center mb-4">
<img src="/wp-content/uploads/2023/07/jim_sewell-1.jpg" alt="Jim Sewell" class="img-fluid rounded mb-2" style="max-height:220px">

**[Jim Sewell](/jim/)**
Original student of the L.A. Chinatown school
</div>
<div class="col-md-3 col-sm-6 text-center mb-4">
<img src="/wp-content/uploads/2023/07/bert-sm.jpg" alt="Bert Poe" class="img-fluid rounded mb-2" style="max-height:220px">

**[Bert Poe](/bert/)**
Marine Raider, Sheriff, Pro Boxer, and Bodyguard
</div>
</div>

<div class="row">
<div class="col-md-3 col-sm-6 text-center mb-4">
<img src="/wp-content/uploads/2023/07/sonny_bygum-1.jpg" alt="Sonny Bygum" class="img-fluid rounded mb-2" style="max-height:220px">

**[Sonny Bygum](/sonny/)**
Navy Seal, Boxer, and Automobile & Motorcycle Racer
</div>
<div class="col-md-3 col-sm-6 text-center mb-4">
<img src="/wp-content/uploads/2023/07/blue.jpg" alt="D.M. Blue" class="img-fluid rounded mb-2" style="max-height:220px">

**[D.M. Blue](/dennis/)**
Instrumental in training the current generation of Instructors
</div>
<div class="col-md-3 col-sm-6 text-center mb-4">
<img src="/wp-content/uploads/2023/07/lynch.jpg" alt="Jeremy Lynch" class="img-fluid rounded mb-2" style="max-height:220px">

**[Jeremy Lynch](/jeremy/)**
Has been with the group since he was just 19 years old
</div>
</div>

---

## Members

<div class="row">
<div class="col-md-3 col-sm-6 text-center mb-4">
<img src="/wp-content/uploads/2023/07/raimondi.jpg" alt="Vince Raimondi" class="img-fluid rounded mb-2" style="max-height:220px">

**[Vince Raimondi](/vince/)**
</div>
<div class="col-md-3 col-sm-6 text-center mb-4">
<img src="/wp-content/uploads/2023/07/lance.jpg" alt="Brent Lance" class="img-fluid rounded mb-2" style="max-height:220px">

**[Brent Lance](/brent/)**
</div>
<div class="col-md-3 col-sm-6 text-center mb-4">
<img src="/wp-content/uploads/2023/07/loi.jpg" alt="Lak Loi" class="img-fluid rounded mb-2" style="max-height:220px">

**Lak Loi**
</div>
<div class="col-md-3 col-sm-6 text-center mb-4">
<img src="/wp-content/uploads/2023/09/casier_dieter_belgium.jpg" alt="Dieter Casier" class="img-fluid rounded mb-2" style="max-height:220px">

**Dieter Casier**
</div>
</div>

<div class="row">
<div class="col-md-3 col-sm-6 text-center mb-4">
<img src="/wp-content/uploads/2023/07/thornton.jpg" alt="Mick Thornton" class="img-fluid rounded mb-2" style="max-height:220px">

**Mick Thornton**
</div>
<div class="col-md-3 col-sm-6 text-center mb-4">
<img src="/wp-content/uploads/2023/07/jmccann.jpg" alt="Jim McCann" class="img-fluid rounded mb-2" style="max-height:220px">

**[Jim McCann](/mccann/)**
</div>
<div class="col-md-3 col-sm-6 text-center mb-4">
<img src="/wp-content/uploads/2023/07/mcgrath.jpg" alt="Tom McGrath" class="img-fluid rounded mb-2" style="max-height:220px">

**Tom McGrath**
</div>
<div class="col-md-3 col-sm-6 text-center mb-4">
<img src="/wp-content/uploads/2023/07/mike.jpg" alt="Mike Blesch" class="img-fluid rounded mb-2" style="max-height:220px">

**[Mike Blesch](/mike/)**
</div>
</div>

<div class="row">
<div class="col-md-3 col-sm-6 text-center mb-4">
<img src="/wp-content/uploads/2023/10/christian-kluge-de.jpg" alt="Christian Kluge" class="img-fluid rounded mb-2" style="max-height:220px">

**Christian Kluge**
</div>
<div class="col-md-3 col-sm-6 text-center mb-4">
<img src="/wp-content/uploads/2023/09/cedomir_pusica.jpg" alt="Cedomir Pusica" class="img-fluid rounded mb-2" style="max-height:220px">

**Cedomir Pusica**
</div>
</div>
```

- [ ] **Step 2: Verify image files exist**

```bash
for img in bob_bremer-2.jpg tim_tackett-1.jpg jim_sewell-1.jpg bert-sm.jpg \
           sonny_bygum-1.jpg blue.jpg lynch.jpg raimondi.jpg lance.jpg loi.jpg \
           jmccann.jpg mcgrath.jpg mike.jpg thornton.jpg; do
  ls "/c/Users/Bitpusher/workspace/jkdpower.github.io/wp-content/uploads/2023/07/$img" 2>&1
done
```

If any image is missing, check `wp-content/uploads/2023/07/` for the correct filename and update the `members.md` accordingly.

- [ ] **Step 3: Build and verify**

```bash
bundle exec jekyll build --strict_front_matter 2>&1 | tail -10
ls _site/members/
```

- [ ] **Step 4: Commit**

```bash
git add _sitepages/members.md
git commit -m "feat: rewrite members.md to clean Markdown photo grid"
```

---

## Task 8: Rewrite `seminars.md`

**Files:**
- Modify: `_sitepages/seminars.md`

Current file has a SiteOrigin blog-post-list widget. Replace with a clean page that links to seminar posts.

- [ ] **Step 1: Replace `_sitepages/seminars.md`**

```markdown
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
```

- [ ] **Step 2: Build and verify**

```bash
bundle exec jekyll build --strict_front_matter 2>&1 | tail -10
ls _site/seminars/
```

- [ ] **Step 3: Commit**

```bash
git add _sitepages/seminars.md
git commit -m "feat: rewrite seminars.md with Liquid event listing"
```

---

## Task 9: Rewrite `official.md`

**Files:**
- Modify: `_sitepages/official.md`

The current file is ~19KB of SiteOrigin HTML containing instructor listings. Reference https://jkdwednite.com/official/ for the current content.

- [ ] **Step 1: Open the live page for reference**

Open https://jkdwednite.com/official/ in a browser. Note all instructors listed by country/state, their names, locations, and any website links.

- [ ] **Step 2: Replace `_sitepages/official.md`**

Use the following structure, filling in the instructor data from the live page:

```markdown
---
title: 'Official JKD Instructors'
layout: page
image: /wp-content/uploads/2023/07/TTBB-color.jpg
header_type: hero
permalink: /official/
include_on_search: true
show_author: false
---

Official Instructors teach the Wednesday Night Group's brand of [Jeet Kune Do](/jeet-kune-do/). We also have [Affiliates](/affiliated/) that may teach some WNG JKD combined with material from other sources.

---

## United States

### California {#california}

| Instructor | Location | Contact |
|------------|----------|---------|
| [Jeremy Lynch](/jeremy/) | Yucaipa, CA | jkdjeremy@gmail.com |
| [Dennis Blue](/dennis/) | ... | ... |
<!-- Add remaining CA instructors from live site -->

### Colorado {#colorado}

<!-- Add instructors from live site -->

<!-- Continue for all US states listed on the live page -->

---

## Europe

### Belgium {#belgium}

<!-- Add instructors from live site -->

<!-- Continue for all European countries -->
```

Fill in all instructor data from the live site before committing.

- [ ] **Step 3: Build and verify**

```bash
bundle exec jekyll build --strict_front_matter 2>&1 | tail -10
ls _site/official/
```

- [ ] **Step 4: Commit**

```bash
git add _sitepages/official.md
git commit -m "feat: rewrite official.md with clean instructor table"
```

---

## Task 10: Rewrite instructor profile pages

**Files (17 pages):**
`bob.md`, `tim.md`, `jim.md`, `bert.md`, `sonny.md`, `dennis.md`, `jeremy.md`, `vince.md`, `brent.md`, `mike.md`, `mccann.md`, `hans.md`, `steven.md`, `kwoklyn.md`, `alexander-terra.md`, `nicolas-calluori.md`, `francesco-malfatti.md`

Each page needs: stripped frontmatter, `permalink:`, `header_type: hero`, and clean Markdown body.

- [ ] **Step 1: Extend `clean_pages.py` and run it for instructor pages**

Add these entries to the `pages` dict in `docs/superpowers/tools/clean_pages.py` and re-run:

```python
# Add to the pages dict:
'bob.md':               ('/bob/',               'hero'),
'tim.md':               ('/tim/',               'hero'),
'jim.md':               ('/jim/',               'hero'),
'bert.md':              ('/bert/',              'hero'),
'sonny.md':             ('/sonny/',             'hero'),
'dennis.md':            ('/dennis/',            'hero'),
'jeremy.md':            ('/jeremy/',            'hero'),
'vince.md':             ('/vince/',             'hero'),
'brent.md':             ('/brent/',             'hero'),
'mike.md':              ('/mike/',              'hero'),
'mccann.md':            ('/mccann/',            'hero'),
'hans.md':              ('/hans/',              'hero'),
'steven.md':            ('/steven/',            'hero'),
'kwoklyn.md':           ('/kwoklyn/',           'hero'),
'alexander-terra.md':   ('/alexander-terra/',   'hero'),
'nicolas-calluori.md':  ('/nicolas-calluori/',  'hero'),
'francesco-malfatti.md':('/francesco-malfatti/','hero'),
```

```bash
python docs/superpowers/tools/clean_pages.py
```

- [ ] **Step 2: Clean up WordPress HTML blocks in each instructor page**

The script fixes links and strips frontmatter, but WordPress HTML blocks remain. For each instructor page:

**`<figure class="wp-block-image ...">` blocks** — Convert to plain Markdown images:
```markdown
<!-- Before -->
<figure class="wp-block-image alignleft size-medium is-resized">
![Jeremy Lynch](https://jkdwednite.com/wp-content/uploads/2023/07/lynch-214x300.jpg)
</figure>

<!-- After -->
![Jeremy Lynch](/wp-content/uploads/2023/07/lynch.jpg){: .float-left .mr-3 style="max-width:200px"}
```
Or simply: `![Jeremy Lynch](/wp-content/uploads/2023/07/lynch.jpg)`

**`<figure class="wp-block-embed is-type-video ...">` YouTube embeds** — Replace the raw URL with an HTML embed or a link:
```markdown
<!-- Before -->
<figure class="wp-block-embed is-type-video ...">
<div class="wp-block-embed__wrapper">
https://www.youtube.com/watch?v=Yu978bM46p0
</div>
</figure>

<!-- After — as a simple link -->
[Watch on YouTube](https://www.youtube.com/watch?v=Yu978bM46p0)
```

Check each of the 17 files for these patterns and clean them.

- [ ] **Step 3: Build and spot-check**

```bash
bundle exec jekyll build --strict_front_matter 2>&1 | tail -10
ls _site/jeremy/ _site/bob/ _site/tim/
```

- [ ] **Step 4: Commit**

```bash
git add _sitepages/bob.md _sitepages/tim.md _sitepages/jim.md _sitepages/bert.md \
        _sitepages/sonny.md _sitepages/dennis.md _sitepages/jeremy.md \
        _sitepages/vince.md _sitepages/brent.md _sitepages/mike.md \
        _sitepages/mccann.md _sitepages/hans.md _sitepages/steven.md \
        _sitepages/kwoklyn.md _sitepages/alexander-terra.md \
        _sitepages/nicolas-calluori.md _sitepages/francesco-malfatti.md \
        docs/superpowers/tools/clean_pages.py
git commit -m "feat: add permalinks, strip WP markup from instructor profile pages"
```

---

## Task 11: Normalize post frontmatter

**Files:** All 46 posts in `_posts/`

Each post needs: WP garbage frontmatter stripped, `author:` field normalized from `['Name']` array to `"Name"` string.

- [ ] **Step 1: Write the post normalization script**

Create `docs/superpowers/tools/clean_posts.py`:

```python
#!/usr/bin/env python3
"""Strip WP garbage frontmatter from posts and normalize author field."""

import re
from pathlib import Path

REMOVE_FIELDS = [
    'id', 'guid', 'siteorigin_page_settings', 'siteorigin_premium_meta',
    'two_optimized_date', 'two_page_speed', 'ppma_authors_name',
    'ppma_disable_author_box', 'footnotes',
]

def strip_frontmatter_fields(fm_text: str) -> str:
    lines = fm_text.splitlines(keepends=True)
    result = []
    skipping = False
    for line in lines:
        stripped = line.rstrip('\n\r')
        if stripped and not stripped[0].isspace() and ':' in stripped:
            key = stripped.split(':')[0].strip()
            skipping = key in REMOVE_FIELDS
        elif not stripped.strip():
            skipping = False
        if not skipping:
            result.append(line)
    return ''.join(result)

def normalize_author(fm_text: str) -> str:
    """Convert author: ['Name'] to author: "Name"."""
    def replace_author(m):
        # Extract name from list format: ['Tim Tackett'] or ["Tim Tackett"]
        name_match = re.search(r"""['"](.*?)['"]""", m.group(1))
        if name_match:
            return f'author: "{name_match.group(1)}"'
        return m.group(0)

    return re.sub(
        r"^author:\s*(\[.*?\])$",
        replace_author,
        fm_text,
        flags=re.MULTILINE
    )

def fix_links(content: str) -> str:
    content = re.sub(
        r'https://i\d+\.wp\.com/jkdwednite\.com(/wp-content/uploads/[^)"?\s]+)',
        r'\1',
        content
    )
    content = re.sub(
        r'(/wp-content/uploads/[^)"?\s]+)\?[^)">\s]*',
        r'\1',
        content
    )
    content = re.sub(
        r'https?://jkdwednite\.com(/[^)">\s]*)',
        r'\1',
        content
    )
    return content

posts_dir = Path('/c/Users/Bitpusher/workspace/jkdpower.github.io/_posts')
for path in sorted(posts_dir.glob('*.md')):
    text = path.read_text(encoding='utf-8')
    if not text.startswith('---'):
        continue
    end = text.find('\n---', 3)
    if end == -1:
        continue
    fm_text = text[4:end]
    body = text[end+4:]

    fm_text = strip_frontmatter_fields(fm_text)
    fm_text = normalize_author(fm_text)
    body = fix_links(body)

    result = '---\n' + fm_text.lstrip() + '---\n' + body
    path.write_text(result, encoding='utf-8')
    print(f'OK: {path.name}')
```

- [ ] **Step 2: Run the script**

```bash
python docs/superpowers/tools/clean_posts.py
```

Expected: One `OK:` line per post file (46 total).

- [ ] **Step 3: Spot-check a post**

```bash
head -15 _posts/2001-11-27-observing-differences.md
```

Expected: No `siteorigin_*`, `ppma_*`, or `guid:` fields. `author:` should be a plain string like `author: "Tim Tackett"` not an array.

- [ ] **Step 4: Build and verify**

```bash
bundle exec jekyll build --strict_front_matter 2>&1 | tail -10
ls _site/20011127_observing-differences/
```

Expected: Clean build. Post output directory exists.

- [ ] **Step 5: Commit**

```bash
git add _posts/ docs/superpowers/tools/clean_posts.py
git commit -m "feat: strip WP frontmatter and normalize author field in all posts"
```

---

## Task 12: Final build verification

- [ ] **Step 1: Full clean build**

```bash
cd /c/Users/Bitpusher/workspace/jkdpower.github.io
rm -rf _site .jekyll-cache
bundle exec jekyll build --strict_front_matter 2>&1
```

Expected: Build completes with no errors. Warnings are acceptable.

- [ ] **Step 2: Check all expected URLs exist**

```bash
for path in "" about contact jeet-kune-do combatives seminars classes \
            articles blog videos gallery books members official affiliated \
            group-news privacy self-defense-blog impact-edge \
            bob tim jim bert sonny dennis jeremy vince brent mike \
            mccann hans steven kwoklyn mccann; do
  echo -n "$path: "
  ls _site/$path/index.html 2>&1 | head -1
done
```

Expected: `index.html` present for each path.

- [ ] **Step 3: Check posts render**

```bash
ls _site/ | grep "^2" | head -10
```

Expected: Multiple `YYYYMMDD_` post directories.

- [ ] **Step 4: Check blog pagination**

```bash
ls _site/blog/
```

Expected: `index.html` and `page2/`, `page3/` directories.

- [ ] **Step 5: Commit verification script output (optional)**

If no issues found, you're done. If issues remain, address the specific build error and re-run.
