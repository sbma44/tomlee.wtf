publish:
	uv run pelican -s publishconf.py content
dev:
	uv run pelican -s pelicanconf.py content && (cd docs && http-server)