publish:
	uv run pelican -s publishconf.py content
	npx pagefind --site docs
dev:
	uv run pelican -s pelicanconf.py content
	npx pagefind --site docs
	cd docs && http-server