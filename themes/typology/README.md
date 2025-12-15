# Typology Pelican Theme

A Pelican theme inspired by the WordPress Typology theme, featuring clean typography and a minimalist layout.

## Features

- **Typography**: Domine (body) and Josefin Sans (headings) fonts from Google Fonts
- **Layout A**: Centered post layout with decorative drop-cap letters
- **Homepage**: Recent posts section (configurable pagination) followed by a year-based archive list
- **Responsive**: Mobile-friendly design with appropriate breakpoints
- **Clean Navigation**: Header with site title and navigation links
- **Archive Views**: Categories, tags, authors, and chronological archives

## Usage

### Installation

The theme is already configured in `pelicanconf.py`:

```python
THEME = 'themes/typology'
DEFAULT_PAGINATION = 20
```

### Building the Site

```bash
uv run pelican content -s pelicanconf.py -o output
```

### Configuration Options

In `pelicanconf.py`:

- `SITENAME`: Your site name (displayed in header)
- `AUTHOR`: Site author name
- `DEFAULT_PAGINATION`: Number of posts per page (default: 20)
- `SOCIAL`: List of social media links for navigation

Example:

```python
SITENAME = "tomlee.wtf"
AUTHOR = "Tom Lee"
DEFAULT_PAGINATION = 20
SOCIAL = (
    ('GitHub', 'https://github.com/yourusername'),
    ('Mastodon', 'https://mastodon.social/@yourusername'),
)
```

### Creating Pages

Create pages in `content/pages/`. For example, for an About page:

```rst
About
#####
:save_as: about/index.html
:url: about/

Your about content here.
```

## Design Elements

### Typography

- **Base font size**: 62.5% (10px = 1rem)
- **Body**: 1.8rem (18px), line-height 1.88
- **H1**: 4.8rem (48px), line-height 1.2
- **H2**: 3.6rem (36px), line-height 1.25
- **H3**: 2.8rem (28px), line-height 1.3

### Layout

- **Content width**: 720px max for article content
- **Section width**: 1170px max for main sections
- **Post spacing**: 9rem bottom margin, 10rem bottom padding
- **Separator lines**: 50px centered horizontal lines between posts

### Drop-cap Letters

Posts display a large decorative first letter (20rem font size) positioned to the left of the content. This is automatically generated from the first character of the post title.

## Templates

- `base.html`: Base template with header/footer
- `index.html`: Homepage with recent posts and archive
- `article.html`: Single post view
- `page.html`: Static page view
- `archives.html`: Chronological archive
- `category.html` / `categories.html`: Category views
- `tag.html` / `tags.html`: Tag views
- `author.html`: Author archive
- `404.html`: Error page

## License

This theme is inspired by the WordPress Typology theme by meks.
