#!/usr/bin/env python3
"""Visualization generator for writing analysis results."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Set style
plt.style.use("seaborn-v0_8-whitegrid")
sns.set_palette("husl")

# Consistent figure size
FIGSIZE_WIDE = (14, 6)
FIGSIZE_SQUARE = (10, 8)
FIGSIZE_TALL = (10, 10)


def save_figure(fig: plt.Figure, output_dir: Path, name: str) -> None:
    """Save figure to PNG."""
    path = output_dir / f"{name}.png"
    fig.savefig(path, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  Saved {path.name}")


def plot_ngram_heatmap(output_dir: Path) -> None:
    """Create heatmap of top n-gram changes over years."""
    for ngram_type in ["unigrams", "bigrams", "trigrams"]:
        csv_path = output_dir / f"ngrams_{ngram_type}_yearly.csv"
        if not csv_path.exists():
            continue

        df = pd.read_csv(csv_path)
        if df.empty:
            continue

        # Get top 15 n-grams by max absolute delta across all periods
        ngram_max_delta = df.groupby("ngram")["delta"].apply(lambda x: x.abs().max())
        top_ngrams = ngram_max_delta.nlargest(15).index.tolist()

        # Filter to top ngrams
        df_top = df[df["ngram"].isin(top_ngrams)]

        # Pivot for heatmap
        pivot = df_top.pivot_table(
            index="ngram", columns="period", values="delta", aggfunc="first"
        )

        # Sort by sum of absolute deltas
        pivot = pivot.loc[pivot.abs().sum(axis=1).sort_values(ascending=False).index]

        fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)
        sns.heatmap(
            pivot,
            cmap="RdBu_r",
            center=0,
            annot=False,
            ax=ax,
            cbar_kws={"label": "Frequency Delta vs 2006"},
        )
        ax.set_title(f"Top {ngram_type.title()} Changes Over Time (vs 2006 Baseline)")
        ax.set_xlabel("Year")
        ax.set_ylabel("N-gram")

        save_figure(fig, output_dir, f"ngrams_{ngram_type}_heatmap")


def plot_word_rarity(output_dir: Path) -> None:
    """Line chart with confidence interval for word rarity."""
    csv_path = output_dir / "word_rarity_yearly.csv"
    if not csv_path.exists():
        return

    df = pd.read_csv(csv_path)
    if df.empty:
        return

    # Ensure period is treated as string
    df["period"] = df["period"].astype(str)

    fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)

    # Plot mean rarity with std as shaded area
    ax.plot(df["period"], df["mean_rarity"], marker="o", linewidth=2, label="Mean Rarity")
    ax.fill_between(
        df["period"],
        df["mean_rarity"] - df["std_rarity"],
        df["mean_rarity"] + df["std_rarity"],
        alpha=0.3,
        label="±1 Std Dev",
    )

    ax.set_xlabel("Year")
    ax.set_ylabel("Rarity Score (higher = rarer vocabulary)")
    ax.set_title("Vocabulary Rarity Over Time")
    ax.legend()
    ax.tick_params(axis="x", rotation=45)

    save_figure(fig, output_dir, "word_rarity_line")


def plot_mtld(output_dir: Path) -> None:
    """Bar chart (yearly) and line chart (quarterly) for MTLD."""
    # Yearly bar chart
    csv_path = output_dir / "mtld_yearly.csv"
    if csv_path.exists():
        df = pd.read_csv(csv_path)
        if not df.empty:
            # Ensure period is treated as string
            df["period"] = df["period"].astype(str)

            fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)

            colors = sns.color_palette("viridis", len(df))
            bars = ax.bar(df["period"], df["mtld"], color=colors)

            ax.set_xlabel("Year")
            ax.set_ylabel("MTLD Score")
            ax.set_title("Lexical Diversity (MTLD) by Year")
            ax.tick_params(axis="x", rotation=45)

            # Add value labels on bars
            for bar, val in zip(bars, df["mtld"]):
                ax.text(
                    bar.get_x() + bar.get_width() / 2,
                    bar.get_height() + 0.5,
                    f"{val:.0f}",
                    ha="center",
                    va="bottom",
                    fontsize=8,
                )

            save_figure(fig, output_dir, "mtld_yearly_bar")

    # Quarterly line chart
    csv_path = output_dir / "mtld_quarterly.csv"
    if csv_path.exists():
        df = pd.read_csv(csv_path)
        if not df.empty:
            fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)

            ax.plot(range(len(df)), df["mtld"], marker=".", linewidth=1.5)
            ax.set_xticks(range(0, len(df), 4))  # Show every 4th label
            ax.set_xticklabels(df["period"].iloc[::4], rotation=45, ha="right")
            ax.set_xlabel("Quarter")
            ax.set_ylabel("MTLD Score")
            ax.set_title("Lexical Diversity (MTLD) by Quarter")

            save_figure(fig, output_dir, "mtld_quarterly_line")


def plot_complexity(output_dir: Path) -> None:
    """Dual-axis line chart for sentence length and clause density."""
    csv_path = output_dir / "complexity_yearly.csv"
    if not csv_path.exists():
        return

    df = pd.read_csv(csv_path)
    if df.empty:
        return

    # Ensure period is treated as string
    df["period"] = df["period"].astype(str)

    fig, ax1 = plt.subplots(figsize=FIGSIZE_WIDE)

    color1 = "#2ecc71"
    color2 = "#e74c3c"

    ax1.set_xlabel("Year")
    ax1.set_ylabel("Avg Sentence Length (words)", color=color1)
    line1 = ax1.plot(
        df["period"],
        df["avg_sentence_length"],
        color=color1,
        marker="o",
        linewidth=2,
        label="Sentence Length",
    )
    ax1.tick_params(axis="y", labelcolor=color1)
    ax1.tick_params(axis="x", rotation=45)

    ax2 = ax1.twinx()
    ax2.set_ylabel("Clause Density (clauses/sentence)", color=color2)
    line2 = ax2.plot(
        df["period"],
        df["clause_density"],
        color=color2,
        marker="s",
        linewidth=2,
        label="Clause Density",
    )
    ax2.tick_params(axis="y", labelcolor=color2)

    # Combined legend
    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc="upper left")

    ax1.set_title("Sentence Complexity Over Time")

    save_figure(fig, output_dir, "complexity_dual_axis")


def plot_pronouns(output_dir: Path) -> None:
    """Stacked area chart for pronoun proportions."""
    csv_path = output_dir / "pronouns_yearly.csv"
    if not csv_path.exists():
        return

    df = pd.read_csv(csv_path)
    if df.empty:
        return

    # Ensure period is treated as string
    df["period"] = df["period"].astype(str)

    fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)

    # Prepare data for stacked area
    categories = [
        ("first_singular_ratio", "I/me/my (1st singular)"),
        ("first_plural_ratio", "we/us/our (1st plural)"),
        ("second_ratio", "you/your (2nd person)"),
        ("third_singular_ratio", "he/she/it (3rd singular)"),
        ("third_plural_ratio", "they/them (3rd plural)"),
    ]

    x = range(len(df))
    y_stack = [df[col].values for col, _ in categories]
    labels = [label for _, label in categories]

    ax.stackplot(x, *y_stack, labels=labels, alpha=0.8)
    ax.set_xticks(x)
    ax.set_xticklabels(df["period"], rotation=45, ha="right")
    ax.set_xlabel("Year")
    ax.set_ylabel("Proportion of Pronouns")
    ax.set_title("Pronoun Usage Over Time")
    ax.legend(loc="upper right", fontsize=8)
    ax.set_ylim(0, 1)

    save_figure(fig, output_dir, "pronouns_stacked_area")


def plot_paragraphs(output_dir: Path) -> None:
    """Box plot for paragraph lengths by year."""
    csv_path = output_dir / "paragraphs_raw_yearly.csv"
    if not csv_path.exists():
        return

    df = pd.read_csv(csv_path)
    if df.empty:
        return

    # Ensure period is treated as string
    df["period"] = df["period"].astype(str)

    # Filter extreme outliers for better visualization
    p99 = df["paragraph_length"].quantile(0.99)
    df_filtered = df[df["paragraph_length"] <= p99]

    fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)

    sns.boxplot(
        data=df_filtered,
        x="period",
        y="paragraph_length",
        hue="period",
        ax=ax,
        palette="Set2",
        legend=False,
    )

    ax.set_xlabel("Year")
    ax.set_ylabel("Paragraph Length (words)")
    ax.set_title("Paragraph Length Distribution by Year")
    ax.tick_params(axis="x", rotation=45)

    save_figure(fig, output_dir, "paragraphs_boxplot")


def plot_words_per_post(output_dir: Path) -> None:
    """Scatter plot with trend line for words per post."""
    csv_path = output_dir / "word_counts_per_post.csv"
    if not csv_path.exists():
        return

    df = pd.read_csv(csv_path)
    if df.empty:
        return

    # Convert date to numeric for regression
    df["date"] = pd.to_datetime(df["date"])
    df["date_num"] = (df["date"] - df["date"].min()).dt.days

    fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)

    # Scatter with transparency
    scatter = ax.scatter(
        df["date"],
        df["words"],
        alpha=0.4,
        s=20,
        c=df["year"],
        cmap="viridis",
    )

    # Add trend line using numpy polyfit
    import numpy as np

    z = np.polyfit(df["date_num"], df["words"], 1)
    p = np.poly1d(z)
    ax.plot(df["date"], p(df["date_num"]), "r--", linewidth=2, label="Trend")

    ax.set_xlabel("Date")
    ax.set_ylabel("Words per Post")
    ax.set_title("Post Length Over Time")
    ax.legend()

    # Colorbar for year (format as integers)
    cbar = plt.colorbar(scatter, ax=ax)
    cbar.set_label("Year")
    cbar.ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f"{int(x)}"))

    save_figure(fig, output_dir, "words_per_post_scatter")


def plot_words_per_period(output_dir: Path) -> None:
    """Bar chart for total words per year."""
    csv_path = output_dir / "word_counts_yearly.csv"
    if not csv_path.exists():
        return

    df = pd.read_csv(csv_path)
    if df.empty:
        return

    # Ensure period is treated as string
    df["period"] = df["period"].astype(str)

    fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)

    colors = sns.color_palette("Blues_d", len(df))
    bars = ax.bar(df["period"], df["total_words"], color=colors)

    ax.set_xlabel("Year")
    ax.set_ylabel("Total Words Written")
    ax.set_title("Writing Volume by Year")
    ax.tick_params(axis="x", rotation=45)

    # Format y-axis with thousands separator
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f"{x:,.0f}"))

    save_figure(fig, output_dir, "words_per_year_bar")


def plot_punctuation(output_dir: Path) -> None:
    """Grouped bar chart for punctuation usage."""
    csv_path = output_dir / "punctuation_yearly.csv"
    if not csv_path.exists():
        return

    df = pd.read_csv(csv_path)
    if df.empty:
        return

    # Ensure period is treated as string
    df["period"] = df["period"].astype(str)

    # Select key punctuation marks
    punct_cols = [
        ("emdash_per_1k", "Em-dash"),
        ("exclamation_per_1k", "Exclamation"),
        ("question_per_1k", "Question"),
        ("semicolon_per_1k", "Semicolon"),
    ]

    fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)

    x = range(len(df))
    width = 0.2
    multiplier = 0

    for col, label in punct_cols:
        offset = width * multiplier
        bars = ax.bar(
            [i + offset for i in x],
            df[col],
            width,
            label=label,
        )
        multiplier += 1

    ax.set_xlabel("Year")
    ax.set_ylabel("Occurrences per 1000 words")
    ax.set_title("Punctuation Usage Over Time")
    ax.set_xticks([i + width * 1.5 for i in x])
    ax.set_xticklabels(df["period"], rotation=45, ha="right")
    ax.legend(loc="upper right")

    save_figure(fig, output_dir, "punctuation_grouped_bar")

    # Also create a line chart for comma usage (most common)
    fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)
    ax.plot(df["period"], df["comma_per_1k"], marker="o", linewidth=2, color="#9b59b6")
    ax.set_xlabel("Year")
    ax.set_ylabel("Commas per 1000 words")
    ax.set_title("Comma Usage Over Time")
    ax.tick_params(axis="x", rotation=45)
    ax.grid(True, alpha=0.3)

    save_figure(fig, output_dir, "punctuation_comma_line")


def plot_post_frequency(output_dir: Path) -> None:
    """Pie chart for posts by year groups."""
    csv_path = output_dir / "word_counts_yearly.csv"
    if not csv_path.exists():
        return

    df = pd.read_csv(csv_path)
    if df.empty:
        return

    # Group into periods
    df["period_int"] = df["period"].astype(int)
    bins = [2005, 2010, 2015, 2020, 2030]
    labels = ["2006-2010", "2011-2015", "2016-2020", "2021+"]
    df["era"] = pd.cut(df["period_int"], bins=bins, labels=labels)

    era_counts = df.groupby("era", observed=True)["post_count"].sum()

    fig, ax = plt.subplots(figsize=(8, 8))

    colors = sns.color_palette("pastel")
    wedges, texts, autotexts = ax.pie(
        era_counts.values,
        labels=era_counts.index,
        autopct="%1.1f%%",
        colors=colors,
        startangle=90,
        explode=[0.02] * len(era_counts),
    )

    ax.set_title("Posts by Era")

    # Add count labels
    for i, (wedge, count) in enumerate(zip(wedges, era_counts.values)):
        angle = (wedge.theta2 - wedge.theta1) / 2 + wedge.theta1
        texts[i].set_text(f"{era_counts.index[i]}\n({count} posts)")

    save_figure(fig, output_dir, "posts_by_era_pie")


def generate_all_visualizations(output_dir: Path) -> None:
    """Generate all visualizations."""
    print("Generating visualizations...")

    print("  N-gram heatmaps...")
    plot_ngram_heatmap(output_dir)

    print("  Word rarity...")
    plot_word_rarity(output_dir)

    print("  MTLD (lexical diversity)...")
    plot_mtld(output_dir)

    print("  Sentence complexity...")
    plot_complexity(output_dir)

    print("  Pronoun usage...")
    plot_pronouns(output_dir)

    print("  Paragraph length...")
    plot_paragraphs(output_dir)

    print("  Words per post...")
    plot_words_per_post(output_dir)

    print("  Words per period...")
    plot_words_per_period(output_dir)

    print("  Punctuation...")
    plot_punctuation(output_dir)

    print("  Post frequency...")
    plot_post_frequency(output_dir)

    print()
    print("All visualizations complete!")


def main() -> None:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Generate visualizations from writing analysis CSVs."
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).parent / "output",
        help="Directory containing CSVs and where PNGs will be saved",
    )

    args = parser.parse_args()
    output_dir = args.output_dir.resolve()

    if not output_dir.is_dir():
        raise SystemExit(f"{output_dir} is not a directory")

    generate_all_visualizations(output_dir)


if __name__ == "__main__":
    main()
