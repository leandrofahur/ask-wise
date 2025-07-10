# ASK WISE - Root Makefile
# Provides unified commands for the entire project

.PHONY: help install test lint format coverage ci clean

# Default target
help:
	@echo "ASK WISE - Available Commands:"
	@echo ""
	@echo "Development:"
	@echo "  install     Install all dependencies"
	@echo "  test        Run all tests"
	@echo "  lint        Run linting checks"
	@echo "  format      Format code with Black"
	@echo "  coverage    Run tests with coverage"
	@echo "  ci          Run complete CI pipeline"
	@echo ""
	@echo "Maintenance:"
	@echo "  clean       Clean generated files"
	@echo ""
	@echo "Server:"
	@echo "  server      Start backend server"
	@echo "  server-install Install server dependencies"
	@echo ""
	@echo "Frontend:"
	@echo "  client Start frontend client"
	@echo "  client-install Install frontend dependencies"
	@echo ""

# Install dependencies
install:
	@echo "Installing backend dependencies..."
	cd backend && uv sync --extra dev --extra server

# Run all tests
test:
	@echo "Running backend tests..."
	cd backend && source .venv/bin/activate && python -m pytest tests/ -v

# Run linting
lint:
	@echo "Running backend linting..."
	cd backend && source .venv/bin/activate && ruff check . --fix

# Format code
format:
	@echo "Formatting backend code..."
	cd backend && source .venv/bin/activate && black .

# Run coverage
coverage:
	@echo "Running backend tests with coverage..."
	cd backend && source .venv/bin/activate && python -m pytest tests/ --cov=core --cov=tests --cov-report=term-missing

# Run complete CI pipeline
ci: lint format test coverage
	@echo "CI pipeline completed successfully!"

# Clean generated files
clean:
	@echo "Cleaning generated files..."
	cd backend && rm -rf .pytest_cache htmlcov .coverage coverage.xml
	rm -rf .ruff_cache
	@echo "Cleanup completed!"

# Backend-specific commands (for direct backend work)
backend-test:
	@echo "Running backend tests..."
	cd backend && make test

backend-lint:
	@echo "Running backend linting..."
	cd backend && make lint

backend-format:
	@echo "Formatting backend code..."
	cd backend && make format

backend-coverage:
	@echo "Running backend coverage..."
	cd backend && make coverage

backend-ci:
	@echo "Running backend CI..."
	cd backend && make ci

# Server commands
server:
	@echo "Starting backend server..."
	cd backend && source .venv/bin/activate && uvicorn main:app --reload --host 0.0.0.0 --port 8000

server-install:
	@echo "Installing server dependencies..."
	cd backend && uv sync --extra dev --extra server 

# Frontend commands
client:
	@echo "Starting frontend server..."
	cd frontend && pnpm dev

client-install:
	@echo "Installing frontend dependencies..."
	cd frontend && pnpm install
