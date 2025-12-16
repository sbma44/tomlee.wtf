"""Word rarity analysis using external corpus frequencies."""

from __future__ import annotations

import re
from typing import TYPE_CHECKING

import pandas as pd

if TYPE_CHECKING:
    from ..parser import Post

try:
    from wordfreq import word_frequency, zipf_frequency
except ImportError:
    # Fallback if wordfreq not installed
    def word_frequency(word: str, lang: str) -> float:
        return 0.0

    def zipf_frequency(word: str, lang: str) -> float:
        return 0.0


WORD_PATTERN = re.compile(r"[a-zA-Z']+")


def tokenize(text: str) -> list[str]:
    """Simple word tokenization."""
    return [w.lower() for w in WORD_PATTERN.findall(text) if len(w) > 1]


def compute_rarity_score(word: str) -> float:
    """
    Compute rarity score for a word.

    Uses Zipf frequency from wordfreq library.
    Zipf scale: 0 = extremely rare, 7+ = very common.
    We invert this so higher = rarer.
    """
    zipf = zipf_frequency(word, "en")
    # Invert: max zipf is around 7-8, so 8 - zipf gives higher scores for rare words
    return max(0, 8 - zipf)


def compute_text_rarity(text: str) -> dict[str, float]:
    """Compute rarity statistics for a text."""
    tokens = tokenize(text)
    if not tokens:
        return {"mean_rarity": 0.0, "median_rarity": 0.0, "rare_word_ratio": 0.0}

    rarity_scores = [compute_rarity_score(w) for w in tokens]

    # Calculate statistics
    mean_rarity = sum(rarity_scores) / len(rarity_scores)

    sorted_scores = sorted(rarity_scores)
    mid = len(sorted_scores) // 2
    if len(sorted_scores) % 2 == 0:
        median_rarity = (sorted_scores[mid - 1] + sorted_scores[mid]) / 2
    else:
        median_rarity = sorted_scores[mid]

    # Ratio of "rare" words (rarity > 5, meaning zipf < 3)
    rare_count = sum(1 for s in rarity_scores if s > 5)
    rare_word_ratio = rare_count / len(rarity_scores)

    return {
        "mean_rarity": mean_rarity,
        "median_rarity": median_rarity,
        "rare_word_ratio": rare_word_ratio,
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
    Compute word rarity metrics for each period.

    Returns DataFrame with columns:
    - period
    - mean_rarity (higher = uses rarer words on average)
    - median_rarity
    - rare_word_ratio (proportion of words with zipf < 3)
    - std_rarity (standard deviation)
    """
    if not posts:
        return pd.DataFrame()

    groups = group_posts_by_period(posts, granularity)

    rows = []
    for period in sorted(groups.keys()):
        period_posts = groups[period]

        # Aggregate all tokens for the period
        all_tokens: list[str] = []
        for post in period_posts:
            all_tokens.extend(tokenize(post.text))

        if not all_tokens:
            continue

        rarity_scores = [compute_rarity_score(w) for w in all_tokens]

        mean_rarity = sum(rarity_scores) / len(rarity_scores)

        sorted_scores = sorted(rarity_scores)
        mid = len(sorted_scores) // 2
        if len(sorted_scores) % 2 == 0:
            median_rarity = (sorted_scores[mid - 1] + sorted_scores[mid]) / 2
        else:
            median_rarity = sorted_scores[mid]

        rare_count = sum(1 for s in rarity_scores if s > 5)
        rare_word_ratio = rare_count / len(rarity_scores)

        # Standard deviation
        variance = sum((s - mean_rarity) ** 2 for s in rarity_scores) / len(
            rarity_scores
        )
        std_rarity = variance**0.5

        rows.append(
            {
                "period": period,
                "mean_rarity": mean_rarity,
                "median_rarity": median_rarity,
                "rare_word_ratio": rare_word_ratio,
                "std_rarity": std_rarity,
                "word_count": len(all_tokens),
            }
        )

    return pd.DataFrame(rows)
