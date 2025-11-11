"""Test file to demonstrate pre-commit hooks."""


def good_function():
    """Calculate sum with proper spacing."""
    x = 1 + 2  # Good spacing
    y = 3 + 4  # Good spacing
    return x + y


def another_good_function():
    """Docstring that respects the 100 character line limit.

    This is now properly formatted.
    """
    pass
