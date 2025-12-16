#!/usr/bin/env python3
"""
Extract WordPress URLs from tomlee.xml and add them as 'url' metadata to RST files.
This preserves the original WordPress permalink structure.
"""

import re
from pathlib import Path

def extract_url_mappings(xml_file):
    """Extract slug -> URL mappings from WordPress export XML."""
    with open(xml_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match posts with links, post_names, and post_type
    pattern = r'<item>.*?<link>(https://tomlee\.wtf/\d{4}/\d{2}/\d{2}/[^/<]+/)</link>.*?<wp:post_name><!\[CDATA\[([^\]]+)\]\]></wp:post_name>.*?<wp:post_type><!\[CDATA\[post\]\]></wp:post_type>.*?</item>'

    matches = re.findall(pattern, content, re.DOTALL)

    # Create slug -> relative path mapping
    url_map = {}
    for url, slug in matches:
        # Extract path from full URL: https://tomlee.wtf/YYYY/MM/DD/slug/ -> YYYY/MM/DD/slug
        url_path = url.replace('https://tomlee.wtf/', '').rstrip('/')
        url_map[slug] = url_path

    return url_map

def add_url_to_rst_file(rst_file, url_path):
    """Add url and save_as metadata fields to RST file if not already present.

    Args:
        rst_file: Path to the RST file
        url_path: Relative URL path like '2022/10/11/aniara'
    """
    with open(rst_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if url field already exists
    has_url = re.search(r'^:url:', content, re.MULTILINE)
    has_save_as = re.search(r'^:save_as:', content, re.MULTILINE)

    if has_url and has_save_as:
        return False  # Already has both fields

    # url_path is already relative like: 2022/10/11/aniara
    # Create save_as path: 2022/10/11/aniara/index.html
    save_as = f'{url_path}/index.html'
    # Create url path: 2022/10/11/aniara/
    url_rel = f'{url_path}/'

    lines = content.split('\n')

    # Find where to insert (after last metadata field, before blank line)
    insert_idx = None
    in_metadata = False

    for i, line in enumerate(lines):
        # Skip title and underline
        if i < 2:
            continue

        # Check if this is a metadata line
        if line.startswith(':') and ':' in line[1:]:
            in_metadata = True
            insert_idx = i + 1
        elif in_metadata and line.strip() == '':
            # Found the blank line after metadata
            break

    if insert_idx is None:
        print(f"  Warning: Could not find metadata section in {rst_file.name}")
        return False

    # Insert the fields (in reverse order since we're inserting at the same index)
    if not has_url:
        lines.insert(insert_idx, f':url: {url_rel}')
    if not has_save_as:
        lines.insert(insert_idx, f':save_as: {save_as}')

    # Write back
    with open(rst_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    return True

def main():
    xml_file = Path('tomlee.xml')
    content_dir = Path('content')

    if not xml_file.exists():
        print(f"Error: {xml_file} not found")
        return

    if not content_dir.exists():
        print(f"Error: {content_dir} not found")
        return

    print("Extracting URL mappings from WordPress export...")
    url_map = extract_url_mappings(xml_file)
    print(f"Found {len(url_map)} post URLs")

    # Process each RST file
    rst_files = list(content_dir.glob('*.rst'))
    print(f"\nProcessing {len(rst_files)} RST files...")

    added_count = 0
    skipped_count = 0
    not_found_count = 0

    for rst_file in sorted(rst_files):
        # Extract slug from RST metadata
        with open(rst_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find :slug: line
        slug_match = re.search(r'^:slug:\s+(.+)$', content, re.MULTILINE)
        if not slug_match:
            print(f"  Warning: No slug found in {rst_file.name}")
            not_found_count += 1
            continue

        slug = slug_match.group(1).strip()

        # Look up URL path
        if slug in url_map:
            url_path = url_map[slug]
            if add_url_to_rst_file(rst_file, url_path):
                added_count += 1
                if added_count <= 5:  # Show first few examples
                    print(f"  {rst_file.name}: {url_path}/")
            else:
                skipped_count += 1
        else:
            # This is expected for drafts and posts without permalinks
            not_found_count += 1

    print(f"\nSummary:")
    print(f"  URLs added: {added_count}")
    print(f"  Already had URL: {skipped_count}")
    print(f"  No URL found (likely drafts): {not_found_count}")

if __name__ == '__main__':
    main()

