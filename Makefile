run:
	poetry run python api/index.py

install:
	pip install poetry
	poetry install
	poetry lock
	poetry run pre-commit install

pre-commit:
	poetry run pre-commit run

bump-version:
	poetry version minor
