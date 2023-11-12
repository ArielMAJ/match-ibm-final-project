ifneq ("$(wildcard .env)","")
	include .env
	export
endif

run:
	poetry run python -m api.index

test:
	poetry run python -m pytest .

install:
	pip install poetry
	poetry install
	poetry lock
	poetry run pre-commit install

pre-commit:
	poetry run pre-commit run

bump-version:
	poetry version minor
