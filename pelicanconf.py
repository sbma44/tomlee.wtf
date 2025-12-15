# Site Information
SITENAME = "Tom Lee"
SITEURL = ""
AUTHOR = "Tom Lee"
TIMEZONE = "America/New_York"

# Output
OUTPUT_PATH = "docs/"

# Theme
THEME = "themes/typology"

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
STATIC_PATHS = ['static']

# Plugins
PLUGINS = ['pelican.plugins.sitemap']

# Sitemap
SITEMAP = {
    'format': 'xml',
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