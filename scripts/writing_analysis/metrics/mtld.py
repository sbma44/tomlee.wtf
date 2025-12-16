"""MTLD (Measure of Textual Lexical Diversity) computation."""

from __future__ import annotations

import re
from typing import TYPE_CHECKING

import pandas as pd

if TYPE_CHECKING:
    from ..parser import Post


WORD_PATTERN = re.compile(r"[a-zA-Z']+")

# TTR threshold for MTLD factor
TTR_THRESHOLD = 0.72


def tokenize(text: str) -> list[str]:
    """Simple word tokenization."""
    return [w.lower() for w in WORD_PATTERN.findall(text) if len(w) > 1]


def compute_mtld_forward(tokens: list[str], threshold: float = TTR_THRESHOLD) -> float:
    """
    Compute MTLD in the forward direction.

    Returns the average number of tokens per factor.
    """
    if len(tokens) < 10:
        return 0.0

    factor_count = 0
    factor_lengths: list[int] = []
    current_types: set[str] = set()
    current_length = 0

    for token in tokens:
        current_types.add(token)
        current_length += 1

        # Calculate current TTR
        ttr = len(current_types) / current_length

        if ttr <= threshold:
            factor_count += 1
            factor_lengths.append(current_length)
            current_types = set()
            current_length = 0

    # Handle remaining tokens (partial factor)
    if current_length > 0:
        final_ttr = len(current_types) / current_length
        # Interpolate partial factor
        partial = (1.0 - final_ttr) / (1.0 - threshold) if threshold < 1.0 else 0
        factor_count += partial
        factor_lengths.append(current_length)

    if factor_count == 0:
        return float(len(tokens))

    return len(tokens) / factor_count


def compute_mtld_bidirectional(tokens: list[str]) -> float:
    """
    Compute MTLD as the average of forward and backward passes.

    MTLD represents the average number of consecutive words in a text
    that maintain a TTR above the threshold.
    """
    if len(tokens) < 10:
        return 0.0

    forward = compute_mtld_forward(tokens)
    backward = compute_mtld_forward(list(reversed(tokens)))

    return (forward + backward) / 2


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
    Compute MTLD for each period.

    Also computes simple TTR for comparison.

    Returns DataFrame with columns:
    - period
    - mtld (Measure of Textual Lexical Diversity)
    - ttr (simple Type-Token Ratio)
    - unique_words
    - total_words
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

        if len(all_tokens) < 10:
            continue

        mtld = compute_mtld_bidirectional(all_tokens)
        unique_words = len(set(all_tokens))
        total_words = len(all_tokens)
        ttr = unique_words / total_words if total_words > 0 else 0

        rows.append(
            {
                "period": period,
                "mtld": mtld,
                "ttr": ttr,
                "unique_words": unique_words,
                "total_words": total_words,
            }
        )

    return pd.DataFrame(rows)
