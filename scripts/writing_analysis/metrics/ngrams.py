"""N-gram analysis with delta comparison to earliest period (2006)."""

from __future__ import annotations

from collections import Counter
from typing import TYPE_CHECKING

import pandas as pd

if TYPE_CHECKING:
    from ..parser import Post

# Simple tokenization - split on whitespace and punctuation, lowercase
import re

WORD_PATTERN = re.compile(r"[a-zA-Z']+")


def tokenize(text: str) -> list[str]:
    """Simple word tokenization."""
    return [w.lower() for w in WORD_PATTERN.findall(text) if len(w) > 1]


def get_ngrams(tokens: list[str], n: int) -> list[tuple[str, ...]]:
    """Extract n-grams from token list."""
    return [tuple(tokens[i : i + n]) for i in range(len(tokens) - n + 1)]


def ngram_frequencies(tokens: list[str], n: int) -> dict[tuple[str, ...], float]:
    """Calculate normalized n-gram frequencies."""
    ngrams = get_ngrams(tokens, n)
    if not ngrams:
        return {}
    counts = Counter(ngrams)
    total = sum(counts.values())
    return {ng: count / total for ng, count in counts.items()}


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


def compute_period_ngrams(
    posts: list["Post"], n: int
) -> dict[tuple[str, ...], float]:
    """Compute aggregate n-gram frequencies for a list of posts."""
    all_tokens: list[str] = []
    for post in posts:
        all_tokens.extend(tokenize(post.text))
    return ngram_frequencies(all_tokens, n)


def compute_deltas(
    baseline: dict[tuple[str, ...], float],
    current: dict[tuple[str, ...], float],
    top_k: int = 50,
) -> list[tuple[tuple[str, ...], float, float, float]]:
    """
    Compute deltas between baseline and current frequencies.
    Returns list of (ngram, baseline_freq, current_freq, delta).
    """
    all_ngrams = set(baseline.keys()) | set(current.keys())

    deltas = []
    for ng in all_ngrams:
        base_freq = baseline.get(ng, 0.0)
        curr_freq = current.get(ng, 0.0)
        delta = curr_freq - base_freq
        deltas.append((ng, base_freq, curr_freq, delta))

    # Sort by absolute delta, descending
    deltas.sort(key=lambda x: abs(x[3]), reverse=True)

    return deltas[:top_k]


def compute(
    posts: list["Post"], granularity: str = "yearly"
) -> dict[str, pd.DataFrame]:
    """
    Compute n-gram analysis for all periods.

    Returns dict with keys like 'unigrams', 'bigrams', 'trigrams',
    each containing a DataFrame with columns:
    - period
    - ngram
    - baseline_freq
    - period_freq
    - delta
    """
    if not posts:
        return {}

    groups = group_posts_by_period(posts, granularity)
    periods = sorted(groups.keys())

    if not periods:
        return {}

    # Get baseline (2006 or earliest available period)
    baseline_period = periods[0]
    baseline_posts = groups[baseline_period]

    results = {}

    for n, name in [(1, "unigrams"), (2, "bigrams"), (3, "trigrams")]:
        baseline_freqs = compute_period_ngrams(baseline_posts, n)

        rows = []
        for period in periods:
            if period == baseline_period:
                continue

            period_freqs = compute_period_ngrams(groups[period], n)
            deltas = compute_deltas(baseline_freqs, period_freqs, top_k=30)

            for ngram, base_freq, curr_freq, delta in deltas:
                ngram_str = " ".join(ngram)
                rows.append(
                    {
                        "period": period,
                        "ngram": ngram_str,
                        "baseline_freq": base_freq,
                        "period_freq": curr_freq,
                        "delta": delta,
                    }
                )

        results[name] = pd.DataFrame(rows)

    return results
