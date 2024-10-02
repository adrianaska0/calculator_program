"""Test Operations"""
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

def test_operation(a, b, operation, expected):
    """Test different operations"""
    calc = Calculation(a, b, operation)
    assert calc.perform() == expected, f"{operation.__name__} operation failed"

def test_divide_by_zero():
    """Test divide by zero exception"""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation = Calculation(Decimal('10'), Decimal('0'), divide)
        calculation.perform()
        