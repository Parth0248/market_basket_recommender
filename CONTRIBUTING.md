# Contributing to Market Basket Recommender

Thank you for your interest in contributing to the Market Basket Recommender System! This document provides guidelines and instructions for contributing to this project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Reporting Bugs](#reporting-bugs)
- [Requesting Features](#requesting-features)
- [Asking Questions](#asking-questions)
- [Code Contributions](#code-contributions)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Pull Request Process](#pull-request-process)
- [Academic Context](#academic-context)

## Code of Conduct

This is an academic project developed for CMPE 256 at San José State University. We expect all contributors to:

- Be respectful and professional
- Provide constructive feedback
- Help maintain a positive learning environment
- Respect academic integrity guidelines

## Getting Started

Before contributing, please:

1. **Read the Documentation**
   - [README.md](README.md) - Complete system overview
   - [QUICKSTART.md](QUICKSTART.md) - Quick start guide
   - [API_EXAMPLES.md](API_EXAMPLES.md) - API usage examples
   - [PROJECT_SUBMISSION.md](PROJECT_SUBMISSION.md) - Project details

2. **Set Up Your Environment**
   ```bash
   # Clone the repository
   git clone https://github.com/Parth0248/market_basket_recommender.git
   cd market_basket_recommender
   
   # Create virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   # Install dependencies
   pip install -r requirements.txt
   
   # Train the model
   python recommender.py
   
   # Test the application
   python app.py
   ```

3. **Explore the Codebase**
   - Familiarize yourself with the project structure
   - Run the application and test its features
   - Review existing issues and pull requests

## How to Contribute

There are several ways to contribute to this project:

### 1. Reporting Bugs 🐛

Found a bug? Help us fix it!

**Before submitting a bug report:**
- Check if the bug has already been reported in [Issues](https://github.com/Parth0248/market_basket_recommender/issues)
- Verify you're using the latest version
- Ensure it's actually a bug and not a feature

**To submit a bug report:**
1. Use the [Bug Report template](.github/ISSUE_TEMPLATE/bug_report.md)
2. Provide a clear title with `[BUG]` prefix
3. Include detailed steps to reproduce
4. Add screenshots or error logs if applicable
5. Specify your environment (OS, Python version, etc.)

### 2. Requesting Features ✨

Have an idea for improvement?

**Before requesting a feature:**
- Check if it's already requested in [Issues](https://github.com/Parth0248/market_basket_recommender/issues)
- Consider if it aligns with the project's goals
- Think about the implementation complexity

**To request a feature:**
1. Use the [Feature Request template](.github/ISSUE_TEMPLATE/feature_request.md)
2. Provide a clear title with `[FEATURE]` prefix
3. Explain the problem it solves
4. Describe your proposed solution
5. Consider alternative approaches
6. Discuss potential implementation ideas

### 3. Asking Questions ❓

Need help or clarification?

**Before asking a question:**
- Check the documentation (README, QUICKSTART, API_EXAMPLES)
- Search existing issues for similar questions
- Try the examples in the documentation

**To ask a question:**
1. Use the [Question template](.github/ISSUE_TEMPLATE/question.md)
2. Provide a clear title with `[QUESTION]` prefix
3. Describe what you're trying to accomplish
4. Share what you've already tried
5. Include relevant code samples or screenshots

## Code Contributions

### Types of Contributions Welcome

- **Bug fixes**: Fix issues identified in the issue tracker
- **Feature implementations**: Add new features discussed in issues
- **Documentation improvements**: Enhance README, comments, or examples
- **Performance optimizations**: Improve recommendation speed or accuracy
- **Test coverage**: Add unit tests or integration tests
- **Code quality**: Refactoring, type hints, or code cleanup

### Development Setup

1. **Fork the Repository**
   - Click "Fork" on GitHub
   - Clone your fork locally

2. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```

3. **Make Your Changes**
   - Follow the coding standards below
   - Add or update tests as needed
   - Update documentation if applicable

4. **Test Your Changes**
   ```bash
   # Train the model
   python recommender.py
   
   # Run the application
   python app.py
   
   # Test API endpoints manually or with automated tests
   ```

## Coding Standards

### Python Code Style

- **PEP 8**: Follow [PEP 8](https://pep8.org/) style guide
- **Type Hints**: Use type hints where possible
- **Docstrings**: Include docstrings for classes and functions
- **Naming Conventions**:
  - Classes: `PascalCase` (e.g., `MarketBasketRecommender`)
  - Functions/methods: `snake_case` (e.g., `get_recommendations`)
  - Constants: `UPPER_CASE` (e.g., `MIN_SUPPORT`)

### Code Organization

```python
# Good example
def get_recommendations(self, cart_items: List[str], top_n: int = 5) -> List[Dict]:
    """
    Get product recommendations based on current cart items
    
    Args:
        cart_items: List of SKUs currently in the cart
        top_n: Number of recommendations to return
        
    Returns:
        List of recommended products with confidence and lift scores
    """
    if not cart_items:
        return []
    
    # Implementation here
```

### Documentation

- **Comments**: Add comments for complex logic
- **README Updates**: Update README.md if adding new features
- **API Documentation**: Update API_EXAMPLES.md for new endpoints
- **Docstrings**: Follow Google or NumPy docstring format

## Testing Guidelines

### Manual Testing

Before submitting a pull request:

1. **Test the Recommendation Engine**
   ```python
   # Test with single item
   cart = ["D7050"]
   recommendations = recommender.get_recommendations(cart)
   
   # Test with multiple items
   cart = ["D7050", "PG9914"]
   recommendations = recommender.get_recommendations(cart)
   
   # Test with empty cart
   cart = []
   recommendations = recommender.get_recommendations(cart)
   ```

2. **Test the Web Interface**
   - Add products to cart
   - Verify recommendations appear
   - Remove products from cart
   - Test edge cases (empty cart, unprecedented combinations)

3. **Test API Endpoints**
   ```bash
   # Health check
   curl http://localhost:8000/health
   
   # Get products
   curl http://localhost:8000/api/products
   
   # Get recommendations
   curl -X POST http://localhost:8000/api/recommendations \
     -H "Content-Type: application/json" \
     -d '{"cart_items": ["D7050"], "top_n": 5}'
   ```

### Automated Testing

If adding automated tests:
- Place test files in a `tests/` directory
- Use `pytest` or `unittest` framework
- Aim for good test coverage
- Test both success and failure cases

## Pull Request Process

### Before Submitting

1. **Update Your Branch**
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Run Final Checks**
   - Code works as expected
   - No linting errors
   - Documentation is updated
   - Tests pass (if applicable)

3. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "Clear, descriptive commit message"
   ```

### Commit Message Guidelines

Use clear, descriptive commit messages:

**Format:**
```
<type>: <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Example:**
```
feat: Add product search functionality

- Implemented search endpoint in FastAPI
- Added search input to web interface
- Updated API documentation with search examples

Closes #42
```

### Submitting the Pull Request

1. **Push to Your Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create Pull Request**
   - Go to GitHub and click "New Pull Request"
   - Select your branch
   - Fill in the PR template:
     - Clear title
     - Description of changes
     - Reference related issues
     - Screenshots (for UI changes)
     - Testing performed

3. **PR Review Process**
   - Maintainers will review your PR
   - Address any feedback or requested changes
   - Be patient and respectful
   - Once approved, your PR will be merged!

## Academic Context

### Important Notes

This project was developed as part of:
- **Course**: CMPE 256 - Recommender Systems
- **University**: San José State University
- **Purpose**: Academic learning and evaluation

### Academic Integrity

- All contributions must be original work
- Properly cite any external sources or libraries
- Do not violate academic integrity policies
- Respect the synthetic nature of the dataset

### Contribution Impact

While this is an academic project, quality contributions can:
- Enhance learning outcomes
- Demonstrate real-world development skills
- Build your portfolio
- Help other students learn

## Questions or Need Help?

- **Documentation**: Check [README.md](README.md), [QUICKSTART.md](QUICKSTART.md)
- **Issues**: Open a [Question issue](.github/ISSUE_TEMPLATE/question.md)
- **Contact**: Reach out to the project team

## Recognition

Contributors will be recognized in:
- Pull request comments
- Project documentation (if significant contribution)
- GitHub contributor statistics

---

## Quick Reference

### Issue Templates
- [Bug Report](.github/ISSUE_TEMPLATE/bug_report.md)
- [Feature Request](.github/ISSUE_TEMPLATE/feature_request.md)
- [Question](.github/ISSUE_TEMPLATE/question.md)

### Key Commands
```bash
# Setup
pip install -r requirements.txt

# Train model
python recommender.py

# Run application
python app.py

# Access application
# Web: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

### Project Structure
```
market_basket_recommender/
├── app.py                      # FastAPI application
├── recommender.py              # Recommendation engine
├── requirements.txt            # Dependencies
├── CONTRIBUTING.md            # This file
├── data/
│   └── transactions.csv       # Transaction data
├── models/
│   └── recommender_model.pkl  # Trained model
└── templates/
    └── index.html             # Web interface
```

---

**Thank you for contributing to the Market Basket Recommender project! 🎉**

Made with ❤️ for SJSU CMPE 256
