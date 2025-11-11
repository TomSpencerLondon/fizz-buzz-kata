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

## Code Quality & Testing

This project uses **pre-commit hooks** to automatically run flake8 (linting) and pytest (tests) before every commit. This ensures code quality and prevents broken code from being committed.

### Running Tests

#### Run all tests
```bash
pytest
```

#### Run tests with coverage
```bash
pytest --cov=src --cov-report=term-missing
```

#### Run tests in watch mode (auto-rerun on file changes)
```bash
ptw
```

#### Run a specific test file
```bash
pytest src/tests/test_fizzbuzz.py
```

#### Run a specific test function
```bash
pytest src/tests/test_fizzbuzz.py::test_1_is_string
```

#### Run tests with verbose output
```bash
pytest -v
```

### Linting

#### Check code style with flake8
```bash
flake8 src/
```

#### Run all pre-commit checks manually
```bash
pre-commit run --all-files
```

### Pre-commit Hooks

Pre-commit hooks are automatically installed and will run before each commit:
- ✅ Trailing whitespace removal
- ✅ End-of-file fixer
- ✅ YAML/TOML validation
- ✅ Large file checker
- ✅ Merge conflict checker
- ✅ **flake8** - Python linting
- ✅ **pytest** - All tests must pass

If any check fails, the commit will be blocked. Fix the issues and try again.

## Project Structure

```
fizz-buzz-kata/
├── src/                          # Source code directory
│   ├── __init__.py
│   ├── fizzbuzz.py              # Your implementation goes here
│   └── tests/                   # Test files
│       ├── __init__.py
│       └── test_fizzbuzz.py     # Your tests go here
├── venv/                         # Virtual environment (gitignored)
├── .flake8                       # Flake8 linting configuration
├── .pre-commit-config.yaml       # Pre-commit hooks configuration
├── pyproject.toml                # Project configuration
├── .gitignore                    # Git ignore rules
├── CLAUDE.md                     # AI pairing guide
├── GITHUB_SETUP.md               # GitHub setup instructions
└── README.md                     # This file
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

# Skip pre-commit hooks for a single commit (not recommended)
git commit --no-verify -m "message"

# Update pre-commit hooks to latest versions
pre-commit autoupdate
```

## Git Configuration

This repository is configured to use your personal GitHub account:
- Email: tomspencerlondon@gmail.com
- Account: TomSpencerLondon

See [GITHUB_SETUP.md](GITHUB_SETUP.md) for details.
