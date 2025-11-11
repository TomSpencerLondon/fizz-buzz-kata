# FizzBuzz Kata (Python)

A TDD implementation of the FizzBuzz kata using Python and pytest.

## Setup

### 1. Activate Virtual Environment

```bash
source venv/bin/activate
```

### 2. Install Dependencies (already done)

```bash
pip install -e ".[dev]"
```

## Running Tests

### Run all tests
```bash
pytest
```

### Run tests with coverage
```bash
pytest --cov=src --cov-report=term-missing
```

### Run tests in watch mode (auto-rerun on file changes)
```bash
ptw
```

### Run a specific test file
```bash
pytest src/tests/test_fizzbuzz.py
```

### Run a specific test function
```bash
pytest src/tests/test_fizzbuzz.py::test_1_is_string
```

### Run tests with verbose output
```bash
pytest -v
```

## Project Structure

```
fizz-buzz-kata/
├── src/                       # Source code directory
│   ├── __init__.py
│   ├── fizzbuzz.py           # Your implementation goes here
│   └── tests/                # Test files
│       ├── __init__.py
│       └── test_fizzbuzz.py  # Your tests go here
├── venv/                      # Virtual environment (gitignored)
├── pyproject.toml             # Project configuration
├── .gitignore                 # Git ignore rules
├── CLAUDE.md                  # AI pairing guide
├── GITHUB_SETUP.md            # GitHub setup instructions
└── README.md                  # This file
```

## TDD Workflow

Follow the Red-Green-Refactor cycle as described in [CLAUDE.md](CLAUDE.md):

1. **Red**: Write a failing test
2. **Green**: Write the simplest code to make it pass
3. **Refactor**: Improve the code without changing behavior
4. **Repeat**

## Quick Start

1. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

2. Start with the first test (already created in `src/tests/test_fizzbuzz.py`)

3. Run tests in watch mode to get instant feedback:
   ```bash
   ptw
   ```

4. Follow the step-by-step guide in [CLAUDE.md](CLAUDE.md)

## Useful Commands

```bash
# Deactivate virtual environment
deactivate

# Run tests with minimal output
pytest -q

# Run tests and stop at first failure
pytest -x

# Run tests matching a pattern
pytest -k "test_fizz"

# Show local variables in tracebacks
pytest -l
```

## Git Configuration

This repository is configured to use your personal GitHub account:
- Email: tomspencerlondon@gmail.com
- Account: TomSpencerLondon

See [GITHUB_SETUP.md](GITHUB_SETUP.md) for details.
