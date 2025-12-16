# Writing Analysis Suite

Tools for analyzing the evolution of writing style across a blog corpus.

## Installation

```bash
cd scripts/writing_analysis
uv sync
```

## Usage

### Run Analysis (generates CSVs)

```bash
cd scripts/writing_analysis
uv run python analyze.py
```

Options:
- `--content-root PATH` - Directory containing posts (default: `../../content`)
- `--output-dir PATH` - Output directory for CSVs (default: `./output`)

### Generate Visualizations (generates PNGs)

```bash
cd scripts/writing_analysis
uv run python visualize.py
```

Options:
- `--output-dir PATH` - Directory with CSVs / where PNGs go (default: `./output`)

## Metrics

| Metric | Description |
|--------|-------------|
| N-gram deltas | Changes in 1/2/3-gram frequency vs 2006 baseline |
| Word rarity | Vocabulary rarity using external corpus (wordfreq) |
| MTLD | Measure of Textual Lexical Diversity |
| Sentence complexity | Average sentence length and clause density |
| Pronoun drift | Changes in I/we/you/they usage proportions |
| Paragraph length | Distribution of paragraph sizes |
| Word counts | Words per post and total per period |
| Punctuation | Em-dash, exclamation, question mark usage |

## Output

All outputs go to `output/`:
- CSV files at yearly, quarterly, and monthly granularity
- PNG visualizations with varied chart types (heatmaps, line charts, bar charts, box plots, scatter plots, pie charts, stacked areas)
