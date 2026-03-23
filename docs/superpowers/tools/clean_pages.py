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

def clean_file(path: Path, permalink: str, header_type: str = None) -> None:
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
    print(f'OK: {path.name}')


if __name__ == '__main__':
    base = Path(__file__).resolve().parent.parent.parent.parent / '_sitepages'

    pages = {
        'about.md':             ('/about/',              'hero'),
        'contact.md':           ('/contact/',             None),
        'jeet-kune-do.md':      ('/jeet-kune-do/',        'hero'),
        'combatives.md':        ('/combatives/',           'hero'),
        'impact-edge.md':       ('/impact-edge/',          None),
        'classes.md':           ('/classes/',              None),
        'videos.md':            ('/videos/',               None),
        'articles.md':          ('/articles/',             None),
        'gallery.md':           ('/gallery/',              None),
        'books.md':             ('/books/',                None),
        'group-news.md':        ('/group-news/',           None),
        'self-defense-blog.md': ('/self-defense-blog/',    None),
        'privacy.md':           ('/privacy/',              None),
        'affiliated.md':        ('/affiliated/',           None),
        'bob.md':               ('/bob/',                 'hero'),
        'tim.md':               ('/tim/',                 'hero'),
        'jim.md':               ('/jim/',                 'hero'),
        'bert.md':              ('/bert/',                'hero'),
        'sonny.md':             ('/sonny/',               'hero'),
        'dennis.md':            ('/dennis/',              'hero'),
        'jeremy.md':            ('/jeremy/',              'hero'),
        'vince.md':             ('/vince/',               'hero'),
        'brent.md':             ('/brent/',               'hero'),
        'mike.md':              ('/mike/',                'hero'),
        'mccann.md':            ('/mccann/',              'hero'),
        'hans.md':              ('/hans/',                'hero'),
        'steven.md':            ('/steven/',              'hero'),
        'kwoklyn.md':           ('/kwoklyn/',             'hero'),
        'alexander-terra.md':   ('/alexander-terra/',     'hero'),
        'nicolas-calluori.md':  ('/nicolas-calluori/',    'hero'),
        'francesco-malfatti.md':('/francesco-malfatti/',  'hero'),
    }

    for filename, (permalink, header_type) in pages.items():
        clean_file(base / filename, permalink, header_type)
