"""Word count analysis: words per post and words per period."""

from __future__ import annotations

import re
from typing import TYPE_CHECKING

import pandas as pd

if TYPE_CHECKING:
    from ..parser import Post


WORD_PATTERN = re.compile(r"[a-zA-Z']+")


def tokenize(text: str) -> list[str]:
    """Simple word tokenization."""
    return [w.lower() for w in WORD_PATTERN.findall(text)]


def count_words(text: str) -> int:
    """Count words in text."""
    return len(tokenize(text))


def group_posts_by_period(
    posts: list["Post"], granularity: str
) -> dict[str, list["Post"]]:
    """Group posts by time period."""
    groups: dict[str, list["Post"]] = {}

    for post in posts:
        if granularity == "yearly":
            key = str(post.year)
        elif granularity == "quarterly":
            key = post.year_quarter
        else:  # monthly
            key = post.year_month

        if key not in groups:
            groups[key] = []
        groups[key].append(post)

    return groups


def percentile(data: list[float], p: float) -> float:
    """Compute percentile of data."""
    if not data:
        return 0.0
    sorted_data = sorted(data)
    k = (len(sorted_data) - 1) * p / 100
    f = int(k)
    c = f + 1 if f + 1 < len(sorted_data) else f
    return sorted_data[f] + (sorted_data[c] - sorted_data[f]) * (k - f)


def compute(posts: list["Post"], granularity: str = "yearly") -> pd.DataFrame:
    """
    Compute word count statistics for each period.

    Returns DataFrame with columns:
    - period
    - total_words (total words written in period)
    - post_count (number of posts in period)
    - avg_words_per_post
    - median_words_per_post
    - min_words_per_post
    - max_words_per_post
    """
    if not posts:
        return pd.DataFrame()

    groups = group_posts_by_period(posts, granularity)

    rows = []
    for period in sorted(groups.keys()):
        period_posts = groups[period]

        word_counts = [count_words(post.text) for post in period_posts]
        word_counts = [c for c in word_counts if c > 0]

        if not word_counts:
            continue

        total_words = sum(word_counts)
        avg_words = total_words / len(word_counts)
        float_counts = [float(x) for x in word_counts]

        rows.append(
            {
                "period": period,
                "total_words": total_words,
                "post_count": len(word_counts),
                "avg_words_per_post": avg_words,
                "median_words_per_post": percentile(float_counts, 50),
                "min_words_per_post": min(word_counts),
                "max_words_per_post": max(word_counts),
            }
        )

    return pd.DataFrame(rows)


def compute_per_post(posts: list["Post"]) -> pd.DataFrame:
    """
    Compute word counts for each individual post (for scatter plots).

    Returns DataFrame with columns:
    - date
    - year
    - words
    - path
    """
    rows = []
    for post in posts:
        words = count_words(post.text)
        if words > 0:
            rows.append(
                {
                    "date": post.date,
                    "year": post.year,
                    "words": words,
                    "path": str(post.path.name),
                }
            )

    return pd.DataFrame(rows)
