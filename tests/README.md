# GAN Test Suite

Comprehensive test suite for the GAN (Great Automatic Nomenclator) package.

## Overview

The test suite contains **53 tests** covering all aspects of the package:

- **CLI tests** (10 tests): Command-line interface, argument parsing, and main function
- **Generation tests** (11 tests): Etymology generation, output rendering (HTML/LaTeX/JSON)
- **Root handling tests** (13 tests): Root joining, vowel elision, protected suffixes
- **I/O tests** (2 tests): Excel file reading and validation
- **Error handling tests** (13 tests): Edge cases, invalid inputs, error conditions
- **Integration tests** (4 tests): End-to-end testing with real test files

## Running Tests

### Basic test run
```bash
pytest
```

### Verbose output
```bash
pytest -v
```

### Run specific test file
```bash
pytest tests/test_cli.py
pytest tests/test_generation.py
```

### Run specific test
```bash
pytest tests/test_cli.py::test_build_parser
```

### Exclude slow tests
```bash
pytest -m "not slow"
```

### Exclude integration tests
```bash
pytest -m "not integration"
```

### Run only integration tests
```bash
pytest -m integration
```

## Test Organization

### `test_cli.py`
Tests for command-line interface functionality:
- Argument parser configuration
- Required and optional arguments
- Main function execution
- Output file generation
- Directory creation

### `test_generation.py`
Tests for core generation logic:
- Etymology combination
- Custom connectors
- Entry generation (2-3 tables)
- JSON/HTML/LaTeX rendering
- Token structure validation

### `test_roots.py`
Tests for root joining and combination:
- Vowel collision handling
- Protected suffix behavior
- Digit stripping
- Empty string handling
- Edge cases (single vowels, long strings)

### `test_io.py`
Tests for Excel file I/O:
- Reading root tables
- Column validation
- Roundtrip (write/read) operations

### `test_errors.py`
Tests for error conditions:
- Missing required columns
- Invalid file formats
- None/NaN handling
- Whitespace trimming
- Duplicate roots
- Special characters
- Very long inputs

### `test_integration.py`
Integration tests using real test files:
- Full pipeline execution
- Real Excel file handling
- Combination count verification
- Large dataset handling (marked as `@pytest.mark.slow`)

## Test Fixtures

Common fixtures available:
- `tmp_path` (pytest built-in): Temporary directory for test files
- `sample_excel` (test_cli.py): Pre-generated Excel test files

## Pytest Configuration

Configuration is in `pyproject.toml`:
```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = ["-v", "--strict-markers", "--strict-config"]
markers = [
    "slow: marks tests as slow",
    "integration: marks tests as integration tests",
]
```

## Coverage

To run with coverage report (requires pytest-cov):
```bash
pip install pytest-cov
pytest --cov=gan_nomenclature --cov-report=html
```

## CI/CD

Tests are automatically run via GitHub Actions on:
- Push to main/master
- Pull requests
- All supported Python versions (check `.github/workflows/ci.yml`)

## Writing New Tests

When adding new tests:
1. Place in appropriate test file based on functionality
2. Use descriptive test names: `test_<what>_<condition>`
3. Add docstrings explaining what is being tested
4. Use fixtures for common setup
5. Mark slow tests with `@pytest.mark.slow`
6. Mark integration tests with `@pytest.mark.integration`

Example:
```python
@pytest.mark.integration
def test_new_feature_with_real_files(tmp_path):
    """Test new feature using real test files."""
    # Test implementation
    pass
```
