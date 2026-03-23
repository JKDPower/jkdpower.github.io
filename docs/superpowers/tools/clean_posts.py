#!/usr/bin/env python3
"""Strip WP garbage frontmatter from posts and normalize author field."""

import re
from pathlib import Path

REMOVE_FIELDS = [
    'id', 'guid', 'siteorigin_page_settings', 'siteorigin_premium_meta',
    'two_optimized_date', 'two_page_speed', 'ppma_authors_name',
    'ppma_disable_author_box', 'footnotes', 'panels_data',
    'siteorigin_panels_data',
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
    """Convert author: ['Name'] or block-list author to author: "Name"."""
    # Handle inline list: author: ['Tim Tackett']
    def replace_author_inline(m):
        name_match = re.search(r"""['"](.*?)['"]""", m.group(1))
        if name_match:
            return f'author: "{name_match.group(1)}"'
        return m.group(0)
    fm_text = re.sub(
        r"^author:\s*(\[.*?\])$",
        replace_author_inline,
        fm_text,
        flags=re.MULTILINE
    )
    # Handle YAML block sequence (one or more items):
    #   author:
    #       - 'Tim Tackett'
    #       - 'Bob Bremer'
    # Keep only the first author name, drop remaining list items.
    def replace_author_block(m):
        first_item_line = m.group(1)  # e.g. "    - 'Tim Tackett'\n"
        name_match = re.search(r"""['"](.*?)['"]""", first_item_line)
        if name_match:
            return f'author: "{name_match.group(1)}"\n'
        bare_match = re.search(r'-\s+(.*)', first_item_line)
        if bare_match:
            return f'author: "{bare_match.group(1).strip()}"\n'
        return m.group(0)
    fm_text = re.sub(
        r"^author:\s*\n([ \t]+-[ \t]+[^\n]*\n)((?:[ \t]+-[ \t]+[^\n]*\n)*)",
        replace_author_block,
        fm_text,
        flags=re.MULTILINE
    )
    return fm_text

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

posts_dir = Path(__file__).resolve().parent.parent.parent.parent / '_posts'
for path in sorted(posts_dir.glob('*.md')):
    text = path.read_text(encoding='utf-8')
    if not text.startswith('---'):
        continue
    end = text.find('\n---', 3)
    glued = text.find('---', 3)
    # If there's a glued --- (no preceding newline) that appears before the first \n---,
    # use it as the actual frontmatter end marker to avoid picking up body horizontal rules.
    if glued != -1 and (end == -1 or glued < end):
        fm_text = text[4:glued]
        rest = text[glued+3:]
        # skip optional newline after ---
        if rest.startswith('\n'):
            rest = rest[1:]
        body = rest
    elif end != -1:
        fm_text = text[4:end]
        body = text[end+4:]
    else:
        continue

    fm_text = strip_frontmatter_fields(fm_text)
    fm_text = normalize_author(fm_text)
    # Remove orphaned list-item lines immediately after a converted author: "..." line
    fm_text = re.sub(
        r'(^author: ".*?"$\n)((?:[ \t]+-[ \t]+[^\n]*\n)+)',
        r'\1',
        fm_text,
        flags=re.MULTILINE
    )
    body = fix_links(body)

    fm_clean = fm_text.lstrip()
    if not fm_clean.endswith('\n'):
        fm_clean += '\n'
    result = '---\n' + fm_clean + '---\n' + body
    path.write_text(result, encoding='utf-8')
    print(f'OK: {path.name}')
