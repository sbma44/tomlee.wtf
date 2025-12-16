"""RST blog post parser with text cleaning for analysis."""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable


@dataclass
class Post:
    """A parsed blog post with cleaned text."""

    path: Path
    date: datetime
    text: str

    @property
    def year(self) -> int:
        return self.date.year

    @property
    def quarter(self) -> int:
        return (self.date.month - 1) // 3 + 1

    @property
    def month(self) -> int:
        return self.date.month

    @property
    def year_quarter(self) -> str:
        return f"{self.year}-Q{self.quarter}"

    @property
    def year_month(self) -> str:
        return f"{self.year}-{self.month:02d}"


# Regex patterns for cleaning
DATE_PATTERN = re.compile(r"^:date:\s*(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2})", re.MULTILINE)
DATE_PATTERN_SHORT = re.compile(r"^:date:\s*(\d{4}-\d{2}-\d{2})", re.MULTILINE)

# Front matter: lines starting with : until first blank line or content
METADATA_LINE = re.compile(r"^:[a-zA-Z_-]+:.*$", re.MULTILINE)

# RST title underlines (sequences of =, -, #, ~, ^, etc.)
TITLE_UNDERLINE = re.compile(r"^[=\-#~^\"\'`]+\s*$", re.MULTILINE)

# RST directives (.. directive:: or .. |name| directive::)
DIRECTIVE_BLOCK = re.compile(
    r"^\.\.\s+(?:\|[^|]+\|\s+)?[a-zA-Z_-]+::[^\n]*(?:\n(?:[ \t]+[^\n]*|\s*))*",
    re.MULTILINE,
)

# RST substitution definitions (.. |name| image:: etc)
SUBSTITUTION_DEF = re.compile(r"^\.\.\s+\|[^|]+\|\s+\w+::[^\n]*(?:\n[ \t]+[^\n]*)*", re.MULTILINE)

# RST inline markup
RST_LINK = re.compile(r"`([^`<]+)\s*<[^>]+>`_+")  # `text <url>`_
RST_LINK_SIMPLE = re.compile(r"`([^`]+)`_+")  # `text`_
RST_EMPHASIS = re.compile(r"\*\*([^*]+)\*\*")  # **bold**
RST_EMPHASIS_SINGLE = re.compile(r"(?<![*\w])\*([^*\n]+)\*(?![*\w])")  # *italic*
RST_LITERAL = re.compile(r"``([^`]+)``")  # ``code``
RST_ROLE = re.compile(r":[a-zA-Z_-]+:`[^`]*`")  # :role:`text`
RST_SUBSCRIPT = re.compile(r":sub:`([^`]*)`")
RST_SUPERSCRIPT = re.compile(r":sup:`([^`]*)`")

# HTML tags
HTML_TAG = re.compile(r"<[^>]+>")

# Reference targets
RST_TARGET = re.compile(r"^\.\.\s+_[^:]+:.*$", re.MULTILINE)

# Raw HTML blocks
RAW_HTML_BLOCK = re.compile(r"^\.\.\s+raw::\s+html\s*\n(?:[ \t]+[^\n]*\n?)*", re.MULTILINE)

# Field list items (used in directives)
FIELD_LIST = re.compile(r"^[ \t]+:[a-zA-Z_-]+:[^\n]*$", re.MULTILINE)

# Multiple blank lines -> single
MULTIPLE_BLANKS = re.compile(r"\n{3,}")

# RST line blocks (lines starting with |)
LINE_BLOCK_PREFIX = re.compile(r"^\|\s?", re.MULTILINE)

# Horizontal rules (----, ====, etc. on their own line)
HORIZONTAL_RULE = re.compile(r"^[-=]{4,}\s*$", re.MULTILINE)


def extract_date(content: str) -> datetime | None:
    """Extract the :date: field from RST content."""
    match = DATE_PATTERN.search(content)
    if match:
        try:
            return datetime.strptime(match.group(1), "%Y-%m-%d %H:%M")
        except ValueError:
            pass

    match = DATE_PATTERN_SHORT.search(content)
    if match:
        try:
            return datetime.strptime(match.group(1), "%Y-%m-%d")
        except ValueError:
            pass

    return None


def clean_text(content: str) -> str:
    """Remove RST markup and HTML, returning clean prose text."""
    text = content

    # Remove the title (first non-empty line) and its underline
    lines = text.split("\n")
    cleaned_lines = []
    in_front_matter = True
    seen_content = False

    for i, line in enumerate(lines):
        stripped = line.strip()

        # Skip title underlines (=== or ### etc)
        if TITLE_UNDERLINE.match(line):
            continue

        # Skip front matter section at the start
        if in_front_matter:
            # Metadata lines like :date:, :author:, etc.
            if METADATA_LINE.match(line):
                continue
            # Empty lines in front matter
            elif stripped == "":
                continue
            # Title line (first non-empty, non-metadata line before we've seen content)
            elif not seen_content and not stripped.startswith(".."):
                # This is likely the title - skip it
                seen_content = True
                # Check if next line is underline - if so, this is definitely title
                if i + 1 < len(lines) and TITLE_UNDERLINE.match(lines[i + 1]):
                    continue
                # If it looks like a title (short, no punctuation at end), skip
                if len(stripped) < 100 and not stripped.endswith((".", "!", "?")):
                    continue
                # Otherwise treat as content
                in_front_matter = False
                cleaned_lines.append(line)
            else:
                in_front_matter = False
                cleaned_lines.append(line)
        else:
            cleaned_lines.append(line)

    text = "\n".join(cleaned_lines)

    # Remove RST directives and blocks
    text = DIRECTIVE_BLOCK.sub("", text)
    text = SUBSTITUTION_DEF.sub("", text)
    text = RST_TARGET.sub("", text)
    text = RAW_HTML_BLOCK.sub("", text)
    text = FIELD_LIST.sub("", text)
    text = HORIZONTAL_RULE.sub("", text)

    # Clean inline markup (preserve the text content)
    text = RST_LINK.sub(r"\1", text)
    text = RST_LINK_SIMPLE.sub(r"\1", text)
    text = RST_LITERAL.sub(r"\1", text)
    text = RST_SUBSCRIPT.sub(r"\1", text)
    text = RST_SUPERSCRIPT.sub(r"\1", text)
    text = RST_ROLE.sub("", text)
    text = RST_EMPHASIS.sub(r"\1", text)
    text = RST_EMPHASIS_SINGLE.sub(r"\1", text)

    # Remove HTML tags
    text = HTML_TAG.sub("", text)

    # Remove RST line block prefixes
    text = LINE_BLOCK_PREFIX.sub("", text)

    # Clean up whitespace
    text = MULTIPLE_BLANKS.sub("\n\n", text)
    text = text.strip()

    return text


def parse_file(path: Path) -> Post | None:
    """Parse a single RST file into a Post."""
    try:
        content = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None

    date = extract_date(content)
    if date is None:
        return None

    text = clean_text(content)
    if not text:
        return None

    return Post(path=path, date=date, text=text)


def iter_rst_files(content_root: Path) -> Iterable[Path]:
    """Iterate over all RST files in the posts directory."""
    posts_dir = content_root / "posts"
    if not posts_dir.exists():
        return

    for path in sorted(posts_dir.rglob("*.rst")):
        yield path


def parse_posts(content_root: Path) -> list[Post]:
    """Parse all blog posts from the content directory."""
    posts: list[Post] = []

    for path in iter_rst_files(content_root):
        post = parse_file(path)
        if post is not None:
            posts.append(post)

    # Sort by date
    posts.sort(key=lambda p: p.date)

    return posts


if __name__ == "__main__":
    import sys

    # Quick test
    root = Path(__file__).parent.parent.parent / "content"
    posts = parse_posts(root)
    print(f"Parsed {len(posts)} posts")
    print(f"Date range: {posts[0].date.date()} to {posts[-1].date.date()}")

    if len(sys.argv) > 1 and sys.argv[1] == "--sample":
        print("\n--- Sample post (first) ---")
        print(f"Path: {posts[0].path}")
        print(f"Date: {posts[0].date}")
        print(f"Text preview: {posts[0].text[:500]}...")
