# Jekyll Migration Design: WordPress → Chulapa on GitHub Pages

**Date:** 2026-03-23
**Project:** jkdpower.github.io
**Original site:** https://jkdwednite.com/

---

## Overview

Migrate a WordPress export of the JKD Wednesday Night Group site to a fully functional Jekyll site hosted on GitHub Pages, using the Chulapa remote theme. All 43 pages and 48 posts are already exported as Markdown files. The work involves fixing configuration, routing, navigation, content cleanup, and internal links so the site builds correctly and looks good in the Chulapa theme.

---

## Section 1: Site Structure & Config

### `_config.yml` updates
- `title`: "JKD Wednesday Night Group"
- `subtitle`: "Preserving and promoting Bruce Lee's art of Jeet Kune Do"
- `description`: "Preserving and promoting Bruce Lee's art of Jeet Kune Do"
- `repository`: `jkdpower/jkdpower.github.io`
- `author.name`: "JKD Wednesday Night Group"
- `author.location`: "Redlands, California"
- Remove `_cheatsheet` collection entry; remove cheatsheet-related defaults and nav items
- Keep `search.provider: fusejs`
- Keep pagination at 4 posts/page at `/blog/page:num/`
- Leave `collections_dir` blank (empty, as currently set)

### Pages collection
**Use collection name `sitepages`** (not `pages`, which is a reserved Jekyll internal variable that Chulapa's templates rely on via `site.pages`).

Add to `collections:` block:
```yaml
sitepages:
  output: true
  permalink: /:name/
```
Remove the `include: _pages` directive (no longer needed). Do this in the same commit as adding the collection, not before.

Add a `defaults` entry for the `sitepages` collection type:
```yaml
- scope:
    path: ""
    type: "sitepages"
  values:
    layout: page
    header_type: base
    show_author: false
    include_on_search: true
```

Each page file gets an explicit `permalink:` in its frontmatter. For most files the permalink matches the filename (e.g. `about.md` → `/about/`). Non-obvious mappings:

| File | Permalink |
|------|-----------|
| `about.md` | `/about/` |
| `affiliated.md` | `/affiliated/` |
| `articles.md` | `/articles/` |
| `bert.md` | `/bert/` |
| `bob.md` | `/bob/` |
| `books.md` | `/books/` |
| `brent.md` | `/brent/` |
| `classes.md` | `/classes/` |
| `combatives.md` | `/combatives/` |
| `contact.md` | `/contact/` |
| `dennis.md` | `/dennis/` |
| `francesco-malfatti.md` | `/francesco-malfatti/` |
| `gallery.md` | `/gallery/` |
| `group-news.md` | `/group-news/` |
| `hans.md` | `/hans/` |
| `impact-edge.md` | `/impact-edge/` |
| `jeet-kune-do.md` | `/jeet-kune-do/` |
| `jeremy.md` | `/jeremy/` |
| `jim.md` | `/jim/` |
| `kwoklyn.md` | `/kwoklyn/` |
| `mccann.md` | `/mccann/` |
| `members.md` | `/members/` |
| `mike.md` | `/mike/` |
| `nicolas-calluori.md` | `/nicolas-calluori/` |
| `official.md` | `/official/` |
| `privacy.md` | `/privacy/` |
| `alexander-terra.md` | `/alexander-terra/` |
| `self-defense-blog.md` | `/self-defense-blog/` |
| `seminars.md` | `/seminars/` |
| `sonny.md` | `/sonny/` |
| `steven.md` | `/steven/` |
| `tim.md` | `/tim/` |
| `videos.md` | `/videos/` |
| `vince.md` | `/vince/` |
| `blog.md` | **DELETE** — redundant with `blog/index.html` (see below) |
| `home-page.md` | **DELETE** — replaced by new `index.md` |
| `cheatsheet.md` | **DELETE** — cheatsheet feature removed |

Key pages with featured images get `header_type: hero` in their individual frontmatter: `about.md`, `jeet-kune-do.md`, `combatives.md`, `members.md`, `seminars.md`, all instructor profile pages.

### Navigation
```
Home | About | Training ▾ | Media ▾ | Members | Contact
```
- **Training** dropdown: Jeet Kune Do (`/jeet-kune-do/`), Combatives (`/combatives/`), Seminars (`/seminars/`), Classes (`/classes/`)
- **Media** dropdown: Articles (`/articles/`), Blog (`/blog/`), Videos (`/videos/`), Gallery (`/gallery/`), Books (`/books/`)
- **Members** links to `/members/`
- **About** links to `/about/`
- **Contact** links to `/contact/`

### Footer
- RSS feed link (keep existing)
- Facebook, Instagram, YouTube social links (matching original site)
- Copyright: © JKD Wednesday Night Group

---

## Section 2: Homepage (`index.md`)

Replace the Chulapa 101 starter content with a page modeled on the original jkdwednite.com homepage.

**Frontmatter:**
```yaml
layout: default
title: "JKD Wednesday Night Group"
subtitle: "Preserve · Promote · Practice"
header_type: hero
image: /wp-content/uploads/2023/08/history-featured.jpg
```

**Body sections:**
1. **Mission statement** — "The purpose of this group is to preserve and promote Bruce Lee's art of Jeet Kune Do, to help define and teach the core curriculum." with a [Get In Touch](/contact/) button
2. **Three training paths** — Bootstrap card row for Old School JKD, Combatives, and Impact & Edged Weapons, each linking to their respective pages
3. **Recent Articles** — Liquid loop showing 4–5 most recent posts from the `Articles` category
4. **Recent News** — Liquid loop showing 3 most recent posts from the `Events` category

---

## Section 3: Page Content Rewrite Strategy

### WordPress frontmatter garbage
All WP-exported pages and posts contain junk frontmatter fields: `siteorigin_page_settings`, `siteorigin_premium_meta`, `two_optimized_date`, `ppma_authors_name`, `ppma_disable_author_box`, `guid`, `footnotes`. These are **in scope to strip** from all files during the content rewrite pass. They are inert to Jekyll but bloat files and clutter the frontmatter.

### Pages requiring full SiteOrigin HTML cleanup → Markdown rewrite

| File | Content to produce |
|------|--------------------|
| `members.md` | Photo grid: founding members + current members, each with name, local image, caption, link to profile page |
| `seminars.md` | Intro text + contact info + links to seminar-category posts |
| `official.md` | List of official instructors with links to their profile pages |
| `affiliated.md` | List of affiliated schools (name, location, instructor, link) |

### Individual instructor profile pages
Files: `bob.md`, `tim.md`, `jim.md`, `bert.md`, `sonny.md`, `dennis.md`, `jeremy.md`, `vince.md`, `brent.md`, `mike.md`, `mccann.md`, `hans.md`, `steven.md`, `kwoklyn.md`, `alexander-terra.md`, `nicolas-calluori.md`, `francesco-malfatti.md`

Each gets: `header_type: hero`, clean Markdown bio, local image reference, stripped WP frontmatter garbage, any relevant links.

### Pages already mostly clean (permalink + minor link fixes + frontmatter strip only)
`about.md`, `contact.md`, `jeet-kune-do.md`, `combatives.md`, `impact-edge.md`, `classes.md`, `videos.md`, `articles.md`, `gallery.md`, `books.md`, `group-news.md`, `self-defense-blog.md`, `privacy.md`

### Internal link rewriting
- All `https://jkdwednite.com/some-page/` → `/some-page/`
- All `https://i0.wp.com/jkdwednite.com/wp-content/uploads/...` → `/wp-content/uploads/...`
- All `https://jkdwednite.com/wp-content/uploads/...` → `/wp-content/uploads/...`

---

## Section 4: Posts & Build Configuration

### Post frontmatter normalization
- `author:` field: normalize from array format `['Tim Tackett']` to string `"Tim Tackett"` for Chulapa compatibility
- Strip WP junk frontmatter fields (same list as pages above) from all posts
- Images already use `/wp-content/uploads/...` — correct, no change needed

### Chulapa defaults for posts (keep existing)
- `header_type: post` (keep)
- `show_author: true`, `show_date: true`, `show_tags: true`, `show_categories: true` (keep)

### Files to DELETE
- `_pages/blog.md` — would collide with `blog/index.html` (the jekyll-paginate driver); the blog index page already works
- `_pages/home-page.md` — replaced by the new `index.md` homepage
- `_pages/cheatsheet.md` — cheatsheet feature removed
- `_posts/2025-10-03-landing-page.md` — Chulapa 101 demo post, not JKD content
- `_posts/2025-10-13-current-skin.md` — Chulapa 101 demo post, not JKD content
- `_cheatsheet/` directory (or just remove from config/nav and exclude from build)

### Files NOT touched
- `_drafts/`
- `_includes/custom/` (giscus, custom head scripts)
- `assets/css/custom.scss`
- `Gemfile` and `Gemfile.lock`
- `.github/` workflows
- `wp-content/` uploads (referenced as static assets)

---

## Out of Scope

- Setting up a custom domain
- Configuring comments (giscus)
- Algolia search indexing
- Google Analytics
- Creating new content
