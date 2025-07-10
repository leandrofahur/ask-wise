lint:
	ruff check . --fix

format:
	black .

lint-fix: format lint

test:
	python -m pytest tests/ -v

coverage:
	python -m pytest tests/ --cov=src --cov=tests --cov-report=term-missing

ci: lint format test coverage
