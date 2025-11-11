"""Tests for FizzBuzz kata.

Following TDD Red-Green-Refactor cycle.
See CLAUDE.md for the step-by-step guide.
"""

from src.fizzbuzz import fizzbuzz_of


def test_1_is_string():
    """Test that 1 returns '1'."""
    assert fizzbuzz_of(1) == "1"


def test_2_is_string():
    """Test that 2 returns '2'."""
    assert fizzbuzz_of(2) == "2"


def test_4_is_string():
    """Test that 4 returns '4'."""
    assert fizzbuzz_of(4) == "4"


def test_3_is_fizz():
    """Test that 3 returns 'Fizz'."""
    assert fizzbuzz_of(3) == "Fizz"


def test_6_is_fizz():
    """Test that 6 returns 'Fizz' (triangulate)."""
    assert fizzbuzz_of(6) == "Fizz"


def test_5_is_buzz():
    """Test that 5 returns 'Buzz'."""
    assert fizzbuzz_of(5) == "Buzz"


def test_10_is_buzz():
    """Test that 10 returns 'Buzz' (triangulate)."""
    assert fizzbuzz_of(10) == "Buzz"
