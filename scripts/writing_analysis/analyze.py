#!/usr/bin/env python3
"""Main CLI runner for writing analysis."""

from __future__ import annotations

import argparse
from pathlib import Path

try:
    # When run as module: python -m scripts.writing_analysis.analyze
    from .parser import parse_posts
    from .metrics import (
        ngrams,
        word_rarity,
        mtld,
        complexity,
        pronouns,
        paragraphs,
        word_counts,
        punctuation,
    )
except ImportError:
    # When run standalone: uv run python analyze.py
    from parser import parse_posts
    from metrics import (
        ngrams,
        word_rarity,
        mtld,
        complexity,
        pronouns,
        paragraphs,
        word_counts,
        punctuation,
    )


def ensure_output_dir(output_dir: Path) -> None:
    """Create output directory if it doesn't exist."""
    output_dir.mkdir(parents=True, exist_ok=True)


def run_analysis(content_root: Path, output_dir: Path) -> None:
    """Run all analyses and save CSVs."""
    print(f"Parsing posts from {content_root}...")
    posts = parse_posts(content_root)
    print(f"Parsed {len(posts)} posts")
    print(f"Date range: {posts[0].date.date()} to {posts[-1].date.date()}")
    print()

    ensure_output_dir(output_dir)

    granularities = ["yearly", "quarterly", "monthly"]

    # N-grams (special handling - returns dict of DataFrames)
    print("Computing n-gram analysis...")
    for granularity in granularities:
        ngram_results = ngrams.compute(posts, granularity)
        for name, df in ngram_results.items():
            if not df.empty:
                path = output_dir / f"ngrams_{name}_{granularity}.csv"
                df.to_csv(path, index=False)
                print(f"  Saved {path.name}")

    # Word rarity
    print("Computing word rarity...")
    for granularity in granularities:
        df = word_rarity.compute(posts, granularity)
        if not df.empty:
            path = output_dir / f"word_rarity_{granularity}.csv"
            df.to_csv(path, index=False)
            print(f"  Saved {path.name}")

    # MTLD
    print("Computing MTLD...")
    for granularity in granularities:
        df = mtld.compute(posts, granularity)
        if not df.empty:
            path = output_dir / f"mtld_{granularity}.csv"
            df.to_csv(path, index=False)
            print(f"  Saved {path.name}")

    # Sentence complexity
    print("Computing sentence complexity...")
    for granularity in granularities:
        df = complexity.compute(posts, granularity)
        if not df.empty:
            path = output_dir / f"complexity_{granularity}.csv"
            df.to_csv(path, index=False)
            print(f"  Saved {path.name}")

    # Pronouns
    print("Computing pronoun analysis...")
    for granularity in granularities:
        df = pronouns.compute(posts, granularity)
        if not df.empty:
            path = output_dir / f"pronouns_{granularity}.csv"
            df.to_csv(path, index=False)
            print(f"  Saved {path.name}")

    # Paragraph length
    print("Computing paragraph length...")
    for granularity in granularities:
        df = paragraphs.compute(posts, granularity)
        if not df.empty:
            path = output_dir / f"paragraphs_{granularity}.csv"
            df.to_csv(path, index=False)
            print(f"  Saved {path.name}")

    # Also save raw lengths for box plots (yearly only to avoid huge files)
    df = paragraphs.compute_raw_lengths(posts, "yearly")
    if not df.empty:
        path = output_dir / "paragraphs_raw_yearly.csv"
        df.to_csv(path, index=False)
        print(f"  Saved {path.name}")

    # Word counts
    print("Computing word counts...")
    for granularity in granularities:
        df = word_counts.compute(posts, granularity)
        if not df.empty:
            path = output_dir / f"word_counts_{granularity}.csv"
            df.to_csv(path, index=False)
            print(f"  Saved {path.name}")

    # Per-post word counts for scatter plot
    df = word_counts.compute_per_post(posts)
    if not df.empty:
        path = output_dir / "word_counts_per_post.csv"
        df.to_csv(path, index=False)
        print(f"  Saved {path.name}")

    # Punctuation
    print("Computing punctuation usage...")
    for granularity in granularities:
        df = punctuation.compute(posts, granularity)
        if not df.empty:
            path = output_dir / f"punctuation_{granularity}.csv"
            df.to_csv(path, index=False)
            print(f"  Saved {path.name}")

    print()
    print(f"All analyses complete. Results saved to {output_dir}")


def main() -> None:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Analyze writing style evolution over time."
    )
    parser.add_argument(
        "--content-root",
        type=Path,
        default=Path(__file__).parent.parent.parent / "content",
        help="Root directory containing posts (default: ../../content)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).parent / "output",
        help="Directory for output CSVs (default: ./output)",
    )

    args = parser.parse_args()

    content_root = args.content_root.resolve()
    if not content_root.is_dir():
        raise SystemExit(f"{content_root} is not a directory")

    output_dir = args.output_dir.resolve()

    run_analysis(content_root, output_dir)


if __name__ == "__main__":
    main()
