#!/usr/bin/env -S uv run python
"""Interactive wizard to create a new draft blog post."""

from __future__ import annotations

import os
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS_ROOT = ROOT / "content" / "posts"

BOLD = "\033[1m"
DIM = "\033[2m"
CYAN = "\033[36m"
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"


def slugify(title: str) -> str:
    s = title.lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_]+", "-", s)
    s = re.sub(r"-+", "-", s)
    return s.strip("-")


def ask(label: str, default: str = "") -> str:
    hint = f" {DIM}({default}){RESET}" if default else ""
    sys.stdout.write(f"  {CYAN}?{RESET} {BOLD}{label}{RESET}{hint}  ")
    sys.stdout.flush()
    value = sys.stdin.readline().strip()
    return value or default


def to_src(img_path: str) -> str:
    """Convert a filesystem path to the web src used in the post."""
    p = Path(img_path).resolve()
    try:
        rel = p.relative_to(ROOT / "content")
        return "/" + rel.as_posix()
    except ValueError:
        return img_path


def main() -> None:
    images = sys.argv[1:]

    print(f"\n  {BOLD}New post{RESET}\n")

    today = date.today().isoformat()
    date_str = ask("Date", today)
    try:
        post_date = date.fromisoformat(date_str)
    except ValueError:
        print(f"\n  {RED}✗{RESET} Invalid date: {date_str!r}", file=sys.stderr)
        sys.exit(1)

    title = ask("Title")
    if not title:
        print(f"\n  {RED}✗{RESET} Title is required.", file=sys.stderr)
        sys.exit(1)

    slug = ask("Slug", slugify(title))

    year = post_date.strftime("%Y")
    post_path = POSTS_ROOT / year / f"{slug}.md"

    if post_path.exists():
        print(f"\n  {RED}✗{RESET} Already exists: {post_path.relative_to(ROOT)}", file=sys.stderr)
        sys.exit(1)

    img_block = (
        "\n" + "\n".join(f'<img src="{to_src(p)}">' for p in images) + "\n"
        if images
        else ""
    )

    front_matter = f"""\
---
title: {title}
date: {date_str}
author: admin
category: Uncategorized
slug: {slug}
status: draft
---
{img_block}"""

    post_path.parent.mkdir(parents=True, exist_ok=True)
    post_path.write_text(front_matter, encoding="utf-8")

    print(f"\n  {GREEN}✓{RESET} {post_path.relative_to(ROOT)}\n")

    editor = os.environ.get("EDITOR", "")
    if editor:
        subprocess.run([editor, str(post_path)])
    else:
        print(f"  Set $EDITOR to open automatically.\n")


if __name__ == "__main__":
    main()
