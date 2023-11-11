run:
	poetry run python app/app.py

install:
	pip install poetry
	poetry install
	poetry lock
	poetry run pre-commit install

pre-commit:
	poetry run pre-commit run
