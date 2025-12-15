#!/usr/bin/env python3
"""Utility helpers for keeping pre-2015 posts marked private."""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parents[1]
POSTS_DIR = REPO_ROOT / "content" / "posts"
EXTRA_DIR = REPO_ROOT / "content" / "extra"
ROBOTS_PATH = EXTRA_DIR / "robots.txt"
DEFAULT_CUTOFF = 2014
DEFAULT_SITEMAP = "https://tomlee.wtf/sitemap.xml"
PRIVATE_LINE = ":private: true"
PRIVATE_LINE_LOWER = PRIVATE_LINE.lower()


def iter_private_posts(cutoff_year: int) -> Iterable[Path]:
    """Yield post paths whose parent year folder is <= cutoff."""
    if not POSTS_DIR.exists():
        raise SystemExit(f"Cannot find posts directory at {POSTS_DIR}")

    for year_dir in sorted(POSTS_DIR.iterdir(), key=lambda p: p.name):
        if not year_dir.is_dir() or not year_dir.name.isdigit():
            continue
        if int(year_dir.name) > cutoff_year:
            continue
        for post in sorted(year_dir.rglob("*.rst")):
            yield post


class MetadataNotFoundError(RuntimeError):
    """Raised when a post body lacks a recognizable metadata block."""


def update_private_metadata(text: str) -> str | None:
    lines = text.splitlines()
    if not lines:
        return None

    trailing_newline = text.endswith("\n")
    private_index = next((i for i, line in enumerate(lines)
                          if line.lower().startswith(":private:")), None)

    if private_index is not None:
        if lines[private_index].strip().lower() == PRIVATE_LINE_LOWER:
            return None
        lines[private_index] = PRIVATE_LINE
    else:
        metadata_start = metadata_end = None
        for idx, line in enumerate(lines):
            if idx < 2:
                continue
            if line.startswith(":") and ":" in line[1:]:
                metadata_start = metadata_start or idx
                metadata_end = idx
            elif metadata_end is not None:
                break

        if metadata_end is None:
            raise MetadataNotFoundError("Unable to locate metadata block")
        insert_at = metadata_end + 1
        lines.insert(insert_at, PRIVATE_LINE)

    new_text = "\n".join(lines)
    if trailing_newline:
        new_text += "\n"
    return new_text


def ensure_private_flag(path: Path, dry_run: bool) -> bool:
    original = path.read_text()
    try:
        updated = update_private_metadata(original)
    except MetadataNotFoundError:
        print(f"Skipping {path.relative_to(REPO_ROOT)} (no metadata found)")
        return False
    if updated is None or updated == original:
        return False
    if not dry_run:
        path.write_text(updated)
    return True


def collect_private_years(cutoff_year: int) -> list[str]:
    years = []
    for year_dir in sorted(POSTS_DIR.iterdir(), key=lambda p: p.name):
        if year_dir.is_dir() and year_dir.name.isdigit():
            if int(year_dir.name) <= cutoff_year:
                years.append(year_dir.name)
    return years


def write_robots_txt(years: Iterable[str], sitemap_url: str | None, dry_run: bool) -> bool:
    lines = ["User-agent: *"]
    for year in years:
        lines.append(f"Disallow: /{year}/")
    if sitemap_url:
        lines.append("")
        lines.append(f"Sitemap: {sitemap_url}")
    content = "\n".join(lines) + "\n"
    if ROBOTS_PATH.exists() and ROBOTS_PATH.read_text() == content:
        return False
    if not dry_run:
        EXTRA_DIR.mkdir(parents=True, exist_ok=True)
        ROBOTS_PATH.write_text(content)
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description="Mark legacy posts as private and refresh robots.txt")
    parser.add_argument("--cutoff", type=int, default=DEFAULT_CUTOFF,
                        help="Highest year to mark as private (default: %(default)s)")
    parser.add_argument("--dry-run", action="store_true", help="Report actions without touching files")
    parser.add_argument("--sitemap", default=DEFAULT_SITEMAP,
                        help="Fully-qualified sitemap URL to include in robots.txt")
    args = parser.parse_args()

    touched = 0
    for post_path in iter_private_posts(args.cutoff):
        if ensure_private_flag(post_path, args.dry_run):
            touched += 1
            print(f"Marked private: {post_path.relative_to(REPO_ROOT)}")

    years = collect_private_years(args.cutoff)
    robots_changed = write_robots_txt(years, args.sitemap, args.dry_run)

    if args.dry_run:
        action = "would update" if touched else "already compliant"
        print(f"Dry run: {action} {touched} posts")
        print("Dry run: robots.txt would", "change" if robots_changed else "stay the same")
    else:
        print(f"Updated {touched} posts")
        print("robots.txt", "updated" if robots_changed else "already current")


if __name__ == "__main__":
    main()
