SHELL := /bin/bash

install:
	pip install poetry
	poetry install
	pre-commit install
