# Thalos Prime v1.0 - Makefile
#
# © 2026 Tony Ray Macier III. All rights reserved.
#
# Common development tasks

.PHONY: help install test lint clean run docker-build docker-run

PYTHON := python3
SRC_DIR := src
TEST_DIR := tests

help:
	@echo "Thalos Prime v1.0 - Development Commands"
	@echo ""
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  help          Show this help message"
	@echo "  install       Install dependencies"
	@echo "  install-dev   Install development dependencies"
	@echo "  test          Run all tests"
	@echo "  test-unit     Run unit tests only"
	@echo "  test-int      Run integration tests only"
	@echo "  lint          Run linting checks"
	@echo "  format        Format code with black"
	@echo "  typecheck     Run type checking with mypy"
	@echo "  clean         Clean build artifacts"
	@echo "  run           Run the main application"
	@echo "  status        Get system status"
	@echo "  docker-build  Build Docker image"
	@echo "  docker-run    Run Docker container"
	@echo "  docker-compose Start with docker-compose"

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt

test: test-unit test-int
	@echo "All tests completed!"

test-unit:
	@echo "Running unit tests..."
	@for test in $(TEST_DIR)/unit/*.py; do \
		if [ "$$(basename $$test)" != "__init__.py" ]; then \
			echo "Running $$test"; \
			$(PYTHON) $$test || exit 1; \
		fi \
	done
	@echo "Unit tests completed!"

test-int:
	@echo "Running integration tests..."
	$(PYTHON) $(TEST_DIR)/integration/test_system.py
	@echo "Integration tests completed!"

test-pytest:
	pytest $(TEST_DIR) -v

lint:
	@echo "Running linting checks..."
	$(PYTHON) -m py_compile $(SRC_DIR)/**/*.py
	$(PYTHON) -m py_compile $(TEST_DIR)/**/*.py
	@echo "Linting completed!"

format:
	black $(SRC_DIR) $(TEST_DIR)
	isort $(SRC_DIR) $(TEST_DIR)

typecheck:
	mypy $(SRC_DIR)

clean:
	@echo "Cleaning build artifacts..."
	rm -rf __pycache__
	rm -rf $(SRC_DIR)/__pycache__
	rm -rf $(SRC_DIR)/**/__pycache__
	rm -rf $(TEST_DIR)/__pycache__
	rm -rf $(TEST_DIR)/**/__pycache__
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf htmlcov
	rm -rf *.egg-info
	rm -rf build
	rm -rf dist
	@echo "Clean completed!"

run:
	$(PYTHON) $(SRC_DIR)/main.py

status:
	$(PYTHON) $(SRC_DIR)/main.py status

boot:
	$(PYTHON) $(SRC_DIR)/main.py boot

memory-list:
	$(PYTHON) $(SRC_DIR)/main.py memory list

docker-build:
	docker build -t thalos-prime:1.0 .

docker-run:
	docker run --rm thalos-prime:1.0 python src/main.py status

docker-compose:
	docker-compose up -d

docker-down:
	docker-compose down

# Development workflow
dev: install-dev lint test
	@echo "Development check completed!"

# CI/CD simulation
ci: lint test
	@echo "CI check completed!"

# Bootstrap
bootstrap:
	chmod +x create_thalos_bootstrap.sh
	./create_thalos_bootstrap.sh
