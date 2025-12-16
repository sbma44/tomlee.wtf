#!/usr/bin/env python3
"""
Scan RST content posts for published entries missing save_as/url directives or
having no body content after the front matter.

This mirrors the Pelican metadata style where front matter is expressed as a
field list (``:field: value``). We only examine the metadata block at the top of
each file and report files marked ``:status: published`` that either lack
``:save_as:``/``:url:`` directives or whose body is entirely whitespace.
"""

from __future__ import annotations

import argparse
import re
import sys
import tempfile
from pathlib import Path

FIELD_RE = re.compile(r"^:([^:]+?):\s*(.*)$")


def _collect_front_matter_lines(path: Path) -> list[str]:
    started = False
    front_matter: list[str] = []
    with path.open("r", encoding="utf-8") as fh:
        for raw in fh:
            trimmed = raw.lstrip()
            if not trimmed:
                continue
            if trimmed.startswith(":") and ":" in trimmed[1:]:
                started = True
                front_matter.append(trimmed)
                continue
            if started:
                break
    return front_matter


def parse_metadata(path: Path) -> dict[str, str]:
    metadata: dict[str, str] = {}
    for line in _collect_front_matter_lines(path):
        match = FIELD_RE.match(line)
        if not match:
            continue
        key, value = match.groups()
        metadata[key.strip().lower()] = value.strip()
    return metadata


def body_is_empty_after_front_matter(path: Path) -> bool:
    """Check if a file has no body content after title and metadata."""
    with path.open("r", encoding="utf-8") as fh:
        lines = [line.rstrip('\n\r') for line in fh]

    # Skip leading blank lines
    idx = 0
    while idx < len(lines) and not lines[idx].strip():
        idx += 1

    if idx >= len(lines):
        return True  # File is entirely blank

    # Check for RST title (text line followed by underline of #, =, -, etc.)
    # or over/underlined title
    title_chars = set('#=-~^"\'`')

    # Check if current line is all title chars (potential overline)
    if lines[idx].strip() and all(c in title_chars for c in lines[idx].strip()):
        # Might be overline, skip it
        idx += 1
        if idx < len(lines):
            idx += 1  # Skip title text
        if idx < len(lines) and all(c in title_chars for c in lines[idx].strip()):
            idx += 1  # Skip underline
    else:
        # Regular title (text + underline)
        idx += 1  # Skip title text
        if idx < len(lines) and lines[idx].strip() and all(c in title_chars for c in lines[idx].strip()):
            idx += 1  # Skip underline

    # Skip blank lines after title
    while idx < len(lines) and not lines[idx].strip():
        idx += 1

    # Now we should be at metadata - skip all lines starting with :field:
    metadata_found = False
    while idx < len(lines):
        stripped = lines[idx].strip()
        if not stripped:
            idx += 1
            continue
        if stripped.startswith(':') and ':' in stripped[1:]:
            metadata_found = True
            idx += 1
            continue
        # Found a non-metadata, non-blank line
        break

    # Skip any blank lines after metadata
    while idx < len(lines) and not lines[idx].strip():
        idx += 1

    # If we've reached the end or only have blank lines, body is empty
    if idx >= len(lines):
        return metadata_found  # Only consider it empty if we found metadata

    # Check if remaining lines are all blank
    for i in range(idx, len(lines)):
        if lines[i].strip():
            return False  # Found non-blank content in body

    return metadata_found


def find_published_issues(content_dir: Path) -> list[tuple[Path, list[str]]]:
    issues: list[tuple[Path, list[str]]] = []
    for rst_path in sorted(content_dir.rglob("*.rst")):
        if not rst_path.is_file():
            continue
        metadata = parse_metadata(rst_path)
        if metadata.get("status", "").lower() != "published":
            continue
        reasons: list[str] = []
        if not (metadata.get("save_as") or metadata.get("url")):
            reasons.append("missing save_as/url metadata")
        if body_is_empty_after_front_matter(rst_path):
            reasons.append("body contains no non-whitespace lines")
        if reasons:
            issues.append((rst_path, reasons))
    return issues


def format_path(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def test_blank_post_detection():
    """Test that we properly detect category.rst as blank."""
    test_content = """Category
########
:date: 2017-03-02 11:45
:author: admin
:slug: category
:status: published
:save_as: 2017/03/02/category/index.html
:url: 2017/03/02/category/


"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.rst', delete=False, encoding='utf-8') as f:
        f.write(test_content)
        temp_path = Path(f.name)

    try:
        result = body_is_empty_after_front_matter(temp_path)
        print(f"Test: category.rst detection - {'PASS' if result else 'FAIL'}")
        print(f"  body_is_empty_after_front_matter returned: {result}")
        if not result:
            print("  Expected: True (body should be detected as empty)")
            print("  This post has only title and metadata, no body content")
    finally:
        temp_path.unlink()

    return result


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(
        description="Find published RST posts missing save_as/url metadata or body content."
    )
    parser.add_argument(
        "--content-dir",
        type=Path,
        default=repo_root / "content",
        help="Path to the content directory to scan.",
    )
    parser.add_argument(
        "--test",
        action="store_true",
        help="Run inline tests to verify detection logic.",
    )
    args = parser.parse_args()

    if args.test:
        print("Running tests...")
        success = test_blank_post_detection()
        return 0 if success else 1

    content_dir = args.content_dir.resolve()
    if not content_dir.exists():
        parser.error(f"{content_dir} does not exist")

    issues = find_published_issues(content_dir)
    if not issues:
        print("All published RST posts have save_as/url metadata and body content.")
        return 0
    print(f"{len(issues)} published RST post(s) have issues:")
    for candidate, reasons in issues:
        print(f"  {format_path(candidate, repo_root)}: {', '.join(reasons)}")

    return 1


if __name__ == "__main__":
    raise SystemExit(main())

