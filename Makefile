PYTHON := python3
VENV := .venv
PIP := $(VENV)/bin/pip
POETRY := $(VENV)/bin/poetry
PYTEST := $(VENV)/bin/pytest

setup:
	$(PIP) install poetry
	@echo "Updating poetry lock file if necessary..."
	$(POETRY) lock
	$(POETRY) install
	$(PIP) install externals/Maeser
	@echo "Maeser setup complete. Running pytests..."
	pytest externals/Maeser/tests