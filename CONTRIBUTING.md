# Contributing to PyLLMTest

First off, thank you for considering contributing to PyLLMTest! It's people like you that make PyLLMTest such a great tool.

## Code of Conduct

This project and everyone participating in it is governed by respect, kindness, and professionalism. By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples** to demonstrate the steps
- **Describe the behavior you observed** and what you expected
- **Include code samples** and error messages
- **Specify your environment** (Python version, OS, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- **Use a clear and descriptive title**
- **Provide a detailed description** of the suggested enhancement
- **Explain why this enhancement would be useful**
- **List some examples** of how it would be used
- **Specify if you'd be willing to implement it**

### Pull Requests

1. **Fork the repo** and create your branch from `main`
2. **Make your changes** with clear, commented code
3. **Add tests** if you're adding functionality
4. **Update documentation** if needed
5. **Ensure tests pass** by running `python tests/test_core.py`
6. **Follow the code style** (use Black for formatting)
7. **Write a clear commit message**

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/pyllmtest.git
cd pyllmtest

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"

# Run tests
python tests/test_core.py
```

## Code Style

- Use **Black** for code formatting: `black pyllmtest/`
- Use **type hints** wherever possible
- Write **docstrings** for all public functions/classes
- Keep functions **focused and small**
- Add **comments** for complex logic

## Adding New Providers

To add a new LLM provider:

1. Create a new file in `pyllmtest/providers/`
2. Inherit from `BaseLLMProvider`
3. Implement all abstract methods
4. Add tests
5. Update documentation

Example:
```python
from pyllmtest.providers.base import BaseLLMProvider

class NewProvider(BaseLLMProvider):
    def complete(self, prompt, **kwargs):
        # Implementation
        pass
```

## Adding New Assertions

To add a new assertion:

1. Add method to `Expectation` class in `pyllmtest/core/assertions.py`
2. Follow naming convention: `to_*` or `not_to_*`
3. Raise `AssertionError` with clear message on failure
4. Add docstring with example
5. Update API_REFERENCE.md

## Testing

- Write tests for new features
- Ensure existing tests pass
- Test both success and failure cases
- Use descriptive test names

## Documentation

- Update README.md if adding major features
- Update API_REFERENCE.md for API changes
- Add examples for new features
- Keep QUICKSTART.md up to date

## Commit Messages

Write clear, descriptive commit messages:

```
Add semantic clustering utility

- Implement cluster_texts() function
- Use k-means algorithm for clustering
- Add tests and documentation
- Update API reference
```

## Project Structure

```
pyllmtest/
├── pyllmtest/           # Main package
│   ├── core/           # Core testing framework
│   ├── providers/      # LLM providers
│   ├── metrics/        # Metrics tracking
│   ├── rag/            # RAG testing
│   ├── optimization/   # Prompt optimization
│   └── utils/          # Utilities
├── tests/              # Test suite
├── examples/           # Examples
└── docs/               # Documentation
```

## Questions?

Feel free to open an issue with the `question` label!

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing to PyLLMTest!** 🚀
