# pylint: disable=unnecessary-dunder-call, invalid-name
"""Module contains tests for the calculator operations and Calculation class"""
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

def test_calculation_operations(a, b, operation, expected):
    """Test operations"""
    c = Calculation(a, b, operation)
    assert c.perform() == expected, f"Failed {operation.__name__} operation with {a} and {b}"

def test_calculation_repr():
    """Test string repr of calculation"""
    c = Calculation(Decimal('10'), Decimal('5'), add)
    expected_repr = "Calculation(10, 5, add)"
    assert c.__repr__() == expected_repr, (
        "The __repr__ method output does not match expected string"
    )

def test_divide_by_zero():
    """Test dividision by zero raises error"""
    c = Calculation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        c.perform()
