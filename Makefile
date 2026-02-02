# Thalos Prime Makefile
# © 2026 Tony Ray Macier III. All rights reserved.

.PHONY: help install install-dev web web-dev test test-unit test-integration coverage lint format type-check clean docker-build docker-run docker-web all

help:
	@echo "Thalos Prime - Development Commands"
	@echo ""
	@echo "Quick Start:"
	@echo "  make web            Launch web interface (production)"
	@echo "  make web-dev        Launch web interface (development)"
	@echo ""
	@echo "Setup:"
	@echo "  make install        Install production dependencies"
	@echo "  make install-dev    Install development dependencies"
	@echo ""
	@echo "Testing:"
	@echo "  make test           Run all tests"
	@echo "  make test-unit      Run unit tests only"
	@echo "  make test-integration  Run integration tests only"
	@echo "  make coverage       Run tests with coverage report"
	@echo ""
	@echo "Code Quality:"
	@echo "  make lint           Run linters (flake8, pylint)"
	@echo "  make format         Format code (black, isort)"
	@echo "  make type-check     Run type checker (mypy)"
	@echo "  make security       Run security checks"
	@echo ""
	@echo "Docker:"
	@echo "  make docker-build   Build Docker image"
	@echo "  make docker-run     Run Docker container"
	@echo "  make docker-web     Run web interface in Docker"
	@echo ""
	@echo "Maintenance:"
	@echo "  make clean          Clean build artifacts"
	@echo "  make all            Run format, lint, type-check, and test"

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

web:
	@echo "🚀 Launching Thalos Prime Web Interface..."
	python boot_thalos.py

web-dev:
	@echo "🚀 Launching Thalos Prime Web Interface (Development Mode)..."
	THALOS_ENV=development THALOS_DEBUG=true python boot_thalos.py

test:
	pytest tests/ -v

test-unit:
	pytest tests/unit/ -v

test-integration:
	pytest tests/integration/ -v

coverage:
	pytest tests/ --cov=src --cov-report=html --cov-report=term-missing

lint:
	@echo "Running flake8..."
	-flake8 src/ tests/ --max-line-length=100 --exclude=__pycache__
	@echo "Running pylint..."
	-pylint src/ --max-line-length=100

format:
	@echo "Running black..."
	black src/ tests/ --line-length=100
	@echo "Running isort..."
	isort src/ tests/ --profile black --line-length=100

type-check:
	mypy src/ --ignore-missing-imports

security:
	@echo "Running bandit security scan..."
	-bandit -r src/ -ll
	@echo "Running safety check..."
	-safety check

docker-build:
	docker build -t thalos-prime:3.0 .

docker-run:
	docker run -p 8000:8000 thalos-prime:3.0

docker-web:
	@echo "🐳 Starting Thalos Prime in Docker..."
	docker-compose up

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	rm -rf build/ dist/ .pytest_cache/ .coverage htmlcov/ .mypy_cache/

all: format lint type-check test
	@echo "All checks completed!"
