# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Site Overview

This is the [JKD Wednesday Night Group](https://jkdpower.github.io) website — a Jekyll static site using the [Chulapa](https://dieghernan.github.io/chulapa/) remote theme, deployed to GitHub Pages via GitHub Actions.

## Commands

```bash
# Install dependencies
bundle install

# Serve locally with live reload
bundle exec jekyll serve --livereload

# Build for production
bundle exec jekyll build

# Build with drafts visible
bundle exec jekyll serve --drafts
```

Deployment is automatic: pushing to `master` or `main` triggers the `build-chulapa-gh-pages.yml` workflow, which builds and deploys to GitHub Pages.

## Architecture

### Content Types

**`_posts/`** — Blog posts with date-prefixed filenames (`YYYY-MM-DD-slug.md`). Front matter includes `title`, `date`, `author`, `permalink`, `image`, `categories`, and `tags`. The `layout: default` + `header_type: hero` combination is standard for posts.

**`_sitepages/`** — Static site pages (About, Classes, Instructors, individual instructor bios, etc.). Rendered with `permalink: /:name/`. Individual instructor pages follow a consistent pattern with a bio, image, and optional YouTube link.

**`index.md`** — Homepage with a Bootstrap carousel (full-width image slides with CTA buttons). Uses `header_type: none` to suppress the default page header.

### Theme and Customization

The site uses `remote_theme: dieghernan/chulapa`. Theme overrides go in:
- `_includes/custom/custom_head.html` — extra `<head>` content (favicons, meta)
- `_includes/custom/custom_bottomscripts.html` — scripts before `</body>`
- `_includes/custom/custom_head_before_css.html` — content before theme CSS
- `assets/css/` — custom CSS

Theme skin colors are set in `_config.yml` under `chulapa-skin.vars` (currently dark navbar `#2d3035`, red links `#b91c1c`).

### Navigation

The navbar is fully defined in `_config.yml` under `navbar.nav`. Dropdown menus use the `child:` key. Adding a new top-level page or dropdown item requires editing `_config.yml`, not individual page files.

### Media Assets

Images are stored under `wp-content/uploads/YYYY/MM/` (migrated from WordPress). New images should follow this convention. Featured/hero images are referenced via the `image:` front matter key.

### Collections

`sitepages` is the only custom collection. Its pages use `permalink: /:name/` which means the filename (without extension) becomes the URL slug.

### Sass / CSS Notes

GitHub Pages uses `jekyll-sass-converter 1.5.2` (LibSass), not Dart Sass. LibSass evaluates `clamp()` arguments as Sass arithmetic, which fails on mixed units like `vw + rem`. Wrap any `clamp()` containing arithmetic in `#{}` interpolation:

```scss
// Wrong — LibSass chokes on mixed units in arithmetic:
font-size: clamp(1rem, 2vw + 0.5rem, 2rem);

// Correct — interpolation passes it through as raw CSS:
font-size: #{clamp(1rem, 2vw + 0.5rem, 2rem)};
```

### Search

Uses Fuse.js (client-side). Pages opt in with `include_on_search: true` in front matter. Posts have this enabled by default via `_config.yml` defaults.

### Pagination

Blog index at `/blog/` paginates at 4 posts per page via `jekyll-paginate`. Paginated URLs follow `/blog/page:num/`.
