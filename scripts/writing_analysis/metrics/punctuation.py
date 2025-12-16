"""Punctuation usage analysis."""

from __future__ import annotations

import re
from typing import TYPE_CHECKING

import pandas as pd

if TYPE_CHECKING:
    from ..parser import Post


WORD_PATTERN = re.compile(r"[a-zA-Z']+")

# Punctuation patterns
EMDASH_PATTERN = re.compile(r"—|--")  # em-dash or double hyphen
EXCLAMATION_PATTERN = re.compile(r"!")
QUESTION_PATTERN = re.compile(r"\?")
SEMICOLON_PATTERN = re.compile(r";")
COLON_PATTERN = re.compile(r":")
COMMA_PATTERN = re.compile(r",")
ELLIPSIS_PATTERN = re.compile(r"\.{3}|…")  # three dots or ellipsis character
PARENTHESES_PATTERN = re.compile(r"[()]")
QUOTES_PATTERN = re.compile(r'[""\'"]')


def count_words(text: str) -> int:
    """Count words in text."""
    return len(WORD_PATTERN.findall(text))


def count_punctuation(text: str) -> dict[str, int]:
    """Count various punctuation marks in text."""
    return {
        "emdash": len(EMDASH_PATTERN.findall(text)),
        "exclamation": len(EXCLAMATION_PATTERN.findall(text)),
        "question": len(QUESTION_PATTERN.findall(text)),
        "semicolon": len(SEMICOLON_PATTERN.findall(text)),
        "colon": len(COLON_PATTERN.findall(text)),
        "comma": len(COMMA_PATTERN.findall(text)),
        "ellipsis": len(ELLIPSIS_PATTERN.findall(text)),
        "parentheses": len(PARENTHESES_PATTERN.findall(text)),
        "quotes": len(QUOTES_PATTERN.findall(text)),
    }


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


def compute(posts: list["Post"], granularity: str = "yearly") -> pd.DataFrame:
    """
    Compute punctuation usage metrics for each period.

    All metrics are normalized per 1000 words.

    Returns DataFrame with columns:
    - period
    - emdash_per_1k
    - exclamation_per_1k
    - question_per_1k
    - semicolon_per_1k
    - colon_per_1k
    - comma_per_1k
    - ellipsis_per_1k
    - parentheses_per_1k
    - quotes_per_1k
    - total_words
    """
    if not posts:
        return pd.DataFrame()

    groups = group_posts_by_period(posts, granularity)

    rows = []
    for period in sorted(groups.keys()):
        period_posts = groups[period]

        # Aggregate counts
        total_counts: dict[str, int] = {
            "emdash": 0,
            "exclamation": 0,
            "question": 0,
            "semicolon": 0,
            "colon": 0,
            "comma": 0,
            "ellipsis": 0,
            "parentheses": 0,
            "quotes": 0,
        }
        total_words = 0

        for post in period_posts:
            counts = count_punctuation(post.text)
            for key, value in counts.items():
                total_counts[key] += value
            total_words += count_words(post.text)

        if total_words == 0:
            continue

        # Normalize to per 1000 words
        factor = 1000 / total_words

        rows.append(
            {
                "period": period,
                "emdash_per_1k": total_counts["emdash"] * factor,
                "exclamation_per_1k": total_counts["exclamation"] * factor,
                "question_per_1k": total_counts["question"] * factor,
                "semicolon_per_1k": total_counts["semicolon"] * factor,
                "colon_per_1k": total_counts["colon"] * factor,
                "comma_per_1k": total_counts["comma"] * factor,
                "ellipsis_per_1k": total_counts["ellipsis"] * factor,
                "parentheses_per_1k": total_counts["parentheses"] * factor,
                "quotes_per_1k": total_counts["quotes"] * factor,
                "total_words": total_words,
            }
        )

    return pd.DataFrame(rows)
