# Makefile

install:
	poetry install
brain-games:
	poetry run brain-games
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
flake:
	poetry add --dev wemake-python-styleguide
lint: flake
	poetry run flake8 brain_games
