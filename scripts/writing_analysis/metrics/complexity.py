"""Sentence complexity and clause density analysis."""

from __future__ import annotations

import re
from typing import TYPE_CHECKING

import pandas as pd

if TYPE_CHECKING:
    from ..parser import Post


# Sentence splitting pattern
SENTENCE_PATTERN = re.compile(r"[.!?]+(?:\s|$)")

# Word pattern
WORD_PATTERN = re.compile(r"[a-zA-Z']+")

# Clause indicators (subordinating conjunctions, relative pronouns, etc.)
CLAUSE_WORDS = {
    "although",
    "because",
    "before",
    "after",
    "while",
    "when",
    "where",
    "which",
    "who",
    "whom",
    "whose",
    "that",
    "if",
    "unless",
    "until",
    "since",
    "though",
    "whereas",
    "whether",
}

# Coordinating conjunctions (can indicate compound sentences)
COORD_CONJUNCTIONS = {"and", "but", "or", "nor", "for", "yet", "so"}


def split_sentences(text: str) -> list[str]:
    """Split text into sentences."""
    # First, normalize whitespace
    text = re.sub(r"\s+", " ", text)

    # Split on sentence-ending punctuation
    sentences = SENTENCE_PATTERN.split(text)

    # Filter empty and very short "sentences"
    return [s.strip() for s in sentences if len(s.strip()) > 5]


def tokenize(text: str) -> list[str]:
    """Simple word tokenization."""
    return [w.lower() for w in WORD_PATTERN.findall(text)]


def count_clauses(sentence: str) -> int:
    """
    Estimate number of clauses in a sentence.

    Uses heuristics:
    - Count subordinating conjunctions
    - Count commas (roughly indicates clause boundaries)
    - Minimum of 1 clause per sentence
    """
    words = tokenize(sentence)
    words_lower = [w.lower() for w in words]

    # Count clause indicators
    clause_word_count = sum(1 for w in words_lower if w in CLAUSE_WORDS)

    # Count commas (clause boundaries)
    comma_count = sentence.count(",")

    # Count semicolons (definitely clause boundaries)
    semicolon_count = sentence.count(";")

    # Base: 1 clause, plus indicators
    # Be conservative: each clause word or semicolon adds 1
    # Commas are less reliable, so weight them lower
    estimated_clauses = 1 + clause_word_count + semicolon_count + (comma_count // 2)

    return estimated_clauses


def compute_text_complexity(text: str) -> dict[str, float]:
    """Compute complexity metrics for a text."""
    sentences = split_sentences(text)

    if not sentences:
        return {
            "avg_sentence_length": 0.0,
            "clause_density": 0.0,
            "sentence_count": 0,
        }

    sentence_lengths: list[int] = []
    clause_counts: list[int] = []

    for sentence in sentences:
        words = tokenize(sentence)
        if words:
            sentence_lengths.append(len(words))
            clause_counts.append(count_clauses(sentence))

    if not sentence_lengths:
        return {
            "avg_sentence_length": 0.0,
            "clause_density": 0.0,
            "sentence_count": 0,
        }

    avg_sentence_length = sum(sentence_lengths) / len(sentence_lengths)
    avg_clauses = sum(clause_counts) / len(clause_counts)

    # Clause density: average clauses per sentence
    clause_density = avg_clauses

    return {
        "avg_sentence_length": avg_sentence_length,
        "clause_density": clause_density,
        "sentence_count": len(sentences),
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
    Compute sentence complexity metrics for each period.

    Returns DataFrame with columns:
    - period
    - avg_sentence_length (words per sentence)
    - clause_density (clauses per sentence)
    - sentence_count
    - std_sentence_length
    """
    if not posts:
        return pd.DataFrame()

    groups = group_posts_by_period(posts, granularity)

    rows = []
    for period in sorted(groups.keys()):
        period_posts = groups[period]

        # Aggregate metrics across all posts in period
        all_sentence_lengths: list[int] = []
        all_clause_counts: list[int] = []

        for post in period_posts:
            sentences = split_sentences(post.text)
            for sentence in sentences:
                words = tokenize(sentence)
                if words:
                    all_sentence_lengths.append(len(words))
                    all_clause_counts.append(count_clauses(sentence))

        if not all_sentence_lengths:
            continue

        avg_sentence_length = sum(all_sentence_lengths) / len(all_sentence_lengths)
        clause_density = sum(all_clause_counts) / len(all_clause_counts)

        # Standard deviation of sentence length
        variance = sum(
            (l - avg_sentence_length) ** 2 for l in all_sentence_lengths
        ) / len(all_sentence_lengths)
        std_sentence_length = variance**0.5

        rows.append(
            {
                "period": period,
                "avg_sentence_length": avg_sentence_length,
                "clause_density": clause_density,
                "sentence_count": len(all_sentence_lengths),
                "std_sentence_length": std_sentence_length,
            }
        )

    return pd.DataFrame(rows)
