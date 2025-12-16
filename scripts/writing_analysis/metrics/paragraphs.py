"""Paragraph length analysis."""

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


def split_paragraphs(text: str) -> list[str]:
    """Split text into paragraphs (separated by blank lines)."""
    # Split on one or more blank lines
    paragraphs = re.split(r"\n\s*\n", text)

    # Filter empty paragraphs and very short ones
    return [p.strip() for p in paragraphs if len(p.strip()) > 10]


def compute_paragraph_lengths(text: str) -> list[int]:
    """Compute word counts for each paragraph."""
    paragraphs = split_paragraphs(text)
    return [len(tokenize(p)) for p in paragraphs if tokenize(p)]


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
    Compute paragraph length statistics for each period.

    Returns DataFrame with columns:
    - period
    - avg_paragraph_length (words per paragraph)
    - median_paragraph_length
    - min_paragraph_length
    - max_paragraph_length
    - p25_paragraph_length (25th percentile)
    - p75_paragraph_length (75th percentile)
    - paragraph_count
    """
    if not posts:
        return pd.DataFrame()

    groups = group_posts_by_period(posts, granularity)

    rows = []
    for period in sorted(groups.keys()):
        period_posts = groups[period]

        # Collect all paragraph lengths
        all_lengths: list[int] = []
        for post in period_posts:
            all_lengths.extend(compute_paragraph_lengths(post.text))

        if not all_lengths:
            continue

        avg_length = sum(all_lengths) / len(all_lengths)
        float_lengths = [float(x) for x in all_lengths]

        rows.append(
            {
                "period": period,
                "avg_paragraph_length": avg_length,
                "median_paragraph_length": percentile(float_lengths, 50),
                "min_paragraph_length": min(all_lengths),
                "max_paragraph_length": max(all_lengths),
                "p25_paragraph_length": percentile(float_lengths, 25),
                "p75_paragraph_length": percentile(float_lengths, 75),
                "paragraph_count": len(all_lengths),
            }
        )

    return pd.DataFrame(rows)


def compute_raw_lengths(
    posts: list["Post"], granularity: str = "yearly"
) -> pd.DataFrame:
    """
    Return raw paragraph lengths for box plot visualization.

    Returns DataFrame with columns:
    - period
    - paragraph_length
    """
    if not posts:
        return pd.DataFrame()

    groups = group_posts_by_period(posts, granularity)

    rows = []
    for period in sorted(groups.keys()):
        period_posts = groups[period]

        for post in period_posts:
            lengths = compute_paragraph_lengths(post.text)
            for length in lengths:
                rows.append({"period": period, "paragraph_length": length})

    return pd.DataFrame(rows)
