"""Metrics modules for writing analysis."""

# Import the modules themselves, not the compute functions
# This allows analyze.py to access module-level functions like compute_raw_lengths
try:
    from . import ngrams
    from . import word_rarity
    from . import mtld
    from . import complexity
    from . import pronouns
    from . import paragraphs
    from . import word_counts
    from . import punctuation
except ImportError:
    import ngrams
    import word_rarity
    import mtld
    import complexity
    import pronouns
    import paragraphs
    import word_counts
    import punctuation

__all__ = [
    "ngrams",
    "word_rarity",
    "mtld",
    "complexity",
    "pronouns",
    "paragraphs",
    "word_counts",
    "punctuation",
]
