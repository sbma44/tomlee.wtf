#!/usr/bin/env -S uv run python
"""
Check that published posts have the required date and slug fields.

These are the only two fields Pelican needs to derive save_as/url via the
global ARTICLE_URL/ARTICLE_SAVE_AS format strings in pelicanconf.py.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

FIELD_RE = re.compile(r"^:([^:]+?):\s*(.*)$")


def parse_rst_metadata(path: Path) -> dict[str, str]:
    metadata: dict[str, str] = {}
    in_metadata = False
    with path.open("r", encoding="utf-8") as fh:
        for raw in fh:
            stripped = raw.strip()
            if not stripped:
                if in_metadata:
                    break
                continue
            m = FIELD_RE.match(stripped)
            if m:
                in_metadata = True
                metadata[m.group(1).strip().lower()] = m.group(2).strip()
            elif in_metadata:
                break
    return metadata


def parse_md_metadata(path: Path) -> dict[str, str] | None:
    with path.open("r", encoding="utf-8") as fh:
        content = fh.read()
    if not content.startswith("---\n"):
        return None
    end = content.find("\n---\n", 4)
    if end == -1:
        return None
    metadata: dict[str, str] = {}
    for line in content[4:end].splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            metadata[key.strip().lower()] = val.strip()
    return metadata


def check_post(path: Path) -> list[str]:
    if path.suffix == ".md":
        meta = parse_md_metadata(path)
    elif path.suffix == ".rst":
        meta = parse_rst_metadata(path)
    else:
        return []

    if not meta or meta.get("status", "").lower() != "published":
        return []

    errors = []
    if not meta.get("date"):
        errors.append("published post is missing 'date'")
    if not meta.get("slug"):
        errors.append("published post is missing 'slug'")
    return errors


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    content_dir = repo_root / "content" / "posts"

    if not content_dir.exists():
        print(f"Content directory not found: {content_dir}", file=sys.stderr)
        return 1

    all_files = sorted(content_dir.rglob("*.md")) + sorted(content_dir.rglob("*.rst"))
    all_errors: list[tuple[Path, list[str]]] = []
    for path in all_files:
        errs = check_post(path)
        if errs:
            all_errors.append((path, errs))

    if not all_errors:
        return 0

    print("Frontmatter errors:", file=sys.stderr)
    for path, errs in all_errors:
        rel = path.relative_to(repo_root)
        for e in errs:
            print(f"  {rel}: {e}", file=sys.stderr)

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
