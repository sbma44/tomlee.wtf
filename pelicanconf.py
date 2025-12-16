from pathlib import Path

# Site Information
SITENAME = "Tom Lee"
AUTHOR = "Tom Lee"
TIMEZONE = "America/New_York"

# Output
OUTPUT_PATH = "docs/"

# Theme
THEME = "themes/typology"

# Legacy/private content handling
BASE_DIR = Path(__file__).parent
POSTS_ROOT = BASE_DIR / "content" / "posts"
PRIVATE_YEAR_CUTOFF = 2014
PRIVATE_YEAR_PREFIXES = tuple(
    f"{path.name}/"
    for path in sorted(POSTS_ROOT.iterdir(), key=lambda p: p.name)
    if path.is_dir() and path.name.isdigit() and int(path.name) <= PRIVATE_YEAR_CUTOFF
) if POSTS_ROOT.exists() else tuple()

# Feeds
FEED_ALL_ATOM = "feed.xml"
FEED_MAX_ITEMS = 20

# Pagination
DEFAULT_PAGINATION = 20
PAGINATION_PATTERNS = (
    (1, '{url}', '{save_as}'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Don't generate slug-based URLs for articles with explicit save_as/url
# This prevents duplicate content at both /slug.html and /YYYY/MM/DD/slug/
ARTICLE_SAVE_AS = ''  # Disable default, rely on per-article save_as metadata
ARTICLE_URL = ''      # Disable default, rely on per-article url metadata

# Static files (images, etc.)
STATIC_PATHS = ['static', 'extra']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

DIRECT_TEMPLATES = ['index']
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAG_SAVE_AS = ''
TAGS_SAVE_AS = ''

# Plugins
PLUGINS = ['pelican.plugins.sitemap']

# Sitemap
SITEMAP = {
    'format': 'xml',
    'exclude': list(PRIVATE_YEAR_PREFIXES),
    'priorities': {
        'articles': 0.6,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Social links (optional - can be customized later)
SOCIAL = (
    ('GitHub', 'https://github.com/sbma44'),
    ('Twitter', 'https://x.com/tjl'),
    ('Bluesky', 'https://bsky.app/profile/tjl.bsky.social')
)

# Theme-specific settings
THEME_STATIC_DIR = 'theme'
THEME_STATIC_PATHS = ['static']
