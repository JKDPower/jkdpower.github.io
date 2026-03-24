#!/usr/bin/env python
"""
Convert Markdown image syntax inside HTML figure blocks to proper <img> tags,
and strip Markdown formatting from <figcaption> content.

Run from repo root:
    python docs/superpowers/tools/fix_images.py
"""

import re
import glob
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent


def md_img_to_html(m):
    alt = m.group(1).strip()
    url_part = m.group(2).strip()
    # Remove optional title attribute: ![alt](url "title")
    url = re.sub(r'\s+"[^"]*"$', '', url_part).strip()
    return f'<img src="{url}" alt="{alt}">'


def clean_figcaption(m):
    tag_open = m.group(1)
    inner = m.group(2)
    tag_close = m.group(3)
    # Strip ***bold italic***, **bold**, *italic*
    inner = re.sub(r'\*\*\*(.+?)\*\*\*', r'\1', inner, flags=re.DOTALL)
    inner = re.sub(r'\*\*(.+?)\*\*', r'\1', inner, flags=re.DOTALL)
    inner = re.sub(r'\*(.+?)\*', r'\1', inner, flags=re.DOTALL)
    return tag_open + inner + tag_close


def fix_file(path):
    content = path.read_text(encoding='utf-8')
    original = content

    # 1. Convert ![alt](url) → <img src="url" alt="alt">
    content = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', md_img_to_html, content)

    # 2. Strip <mark ...>...</mark> wrappers (keep inner text)
    content = re.sub(r'<mark[^>]*>(.*?)</mark>', r'\1', content, flags=re.DOTALL)

    # 3. Clean Markdown formatting inside <figcaption> elements
    content = re.sub(
        r'(<figcaption[^>]*>)(.*?)(</figcaption>)',
        clean_figcaption,
        content,
        flags=re.DOTALL,
    )

    # 4. Strip verbose WP classes from <figcaption class="...">
    content = re.sub(r'<figcaption class="[^"]*">', '<figcaption>', content)

    if content != original:
        path.write_text(content, encoding='utf-8')
        return True
    return False


def main():
    files = (
        list(REPO_ROOT.glob('_posts/*.md'))
        + list(REPO_ROOT.glob('_sitepages/*.md'))
    )
    changed = 0
    for f in files:
        if fix_file(f):
            changed += 1
            print(f'  fixed: {f.name}')
    print(f'\n{changed}/{len(files)} files updated.')


if __name__ == '__main__':
    main()
