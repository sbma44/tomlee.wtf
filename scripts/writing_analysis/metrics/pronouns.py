"""Pronoun usage drift analysis."""

from __future__ import annotations

import re
from typing import TYPE_CHECKING

import pandas as pd

if TYPE_CHECKING:
    from ..parser import Post


WORD_PATTERN = re.compile(r"[a-zA-Z']+")

# Pronoun categories
FIRST_PERSON_SINGULAR = {"i", "me", "my", "mine", "myself"}
FIRST_PERSON_PLURAL = {"we", "us", "our", "ours", "ourselves"}
SECOND_PERSON = {"you", "your", "yours", "yourself", "yourselves"}
THIRD_PERSON_SINGULAR = {"he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself"}
THIRD_PERSON_PLURAL = {"they", "them", "their", "theirs", "themselves"}

ALL_PRONOUNS = (
    FIRST_PERSON_SINGULAR
    | FIRST_PERSON_PLURAL
    | SECOND_PERSON
    | THIRD_PERSON_SINGULAR
    | THIRD_PERSON_PLURAL
)


def tokenize(text: str) -> list[str]:
    """Simple word tokenization."""
    return [w.lower() for w in WORD_PATTERN.findall(text)]


def count_pronouns(tokens: list[str]) -> dict[str, int]:
    """Count pronouns by category."""
    counts = {
        "first_singular": 0,
        "first_plural": 0,
        "second": 0,
        "third_singular": 0,
        "third_plural": 0,
    }

    for token in tokens:
        t = token.lower()
        if t in FIRST_PERSON_SINGULAR:
            counts["first_singular"] += 1
        elif t in FIRST_PERSON_PLURAL:
            counts["first_plural"] += 1
        elif t in SECOND_PERSON:
            counts["second"] += 1
        elif t in THIRD_PERSON_SINGULAR:
            counts["third_singular"] += 1
        elif t in THIRD_PERSON_PLURAL:
            counts["third_plural"] += 1

    return counts


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
    Compute pronoun usage metrics for each period.

    Returns DataFrame with columns:
    - period
    - first_singular_ratio (I/me/my proportion)
    - first_plural_ratio (we/us/our proportion)
    - second_ratio (you/your proportion)
    - third_singular_ratio (he/she/it proportion)
    - third_plural_ratio (they/them proportion)
    - pronoun_density (pronouns per 100 words)
    """
    if not posts:
        return pd.DataFrame()

    groups = group_posts_by_period(posts, granularity)

    rows = []
    for period in sorted(groups.keys()):
        period_posts = groups[period]

        # Aggregate all tokens
        all_tokens: list[str] = []
        for post in period_posts:
            all_tokens.extend(tokenize(post.text))

        if not all_tokens:
            continue

        counts = count_pronouns(all_tokens)
        total_pronouns = sum(counts.values())

        if total_pronouns == 0:
            continue

        rows.append(
            {
                "period": period,
                "first_singular_ratio": counts["first_singular"] / total_pronouns,
                "first_plural_ratio": counts["first_plural"] / total_pronouns,
                "second_ratio": counts["second"] / total_pronouns,
                "third_singular_ratio": counts["third_singular"] / total_pronouns,
                "third_plural_ratio": counts["third_plural"] / total_pronouns,
                "pronoun_density": (total_pronouns / len(all_tokens)) * 100,
                "total_pronouns": total_pronouns,
                "total_words": len(all_tokens),
            }
        )

    return pd.DataFrame(rows)
