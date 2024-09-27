# pylint: disable=unnecessary-dunder-call, invalid-name
"""Calculations Test"""

from decimal import Decimal
import pytest

from calculator.calculation import Calculation
from calculator.calculations import Calculations

from calculator.operations import add, subtract
@pytest.fixture
def setup_calculations():
    """Clear history, add two sample calculations"""
    Calculations.clear_history()
    Calculations.add_calculation(Calculation(Decimal('10'), Decimal('5'), add))
    Calculations.add_calculation(Calculation(Decimal('20'), Decimal('5'), subtract))

def test_add_calculation(setup_calculations):
    """Test adding sample calculations"""
    c = Calculation(Decimal('3'), Decimal('3'), add)
    Calculations.add_calculation(c)
    assert Calculations.get_latest() == c, "Failed to add the calculation to history"

def test_get_history(setup_calculations):
    """Test history recall"""
    history = Calculations.get_history()
    assert len(history) == 2, "History does not have the expected number of calculations"

def test_clear_history(setup_calculations):
    """Test clearing history"""
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0, "History was not cleared"

def test_get_latest(setup_calculations):
    """Test get latest calculation"""
    latest = Calculations.get_latest()
    assert latest.a == Decimal('20') and latest.b == Decimal('5'), "Did not get correct latest calculation"

def test_find_by_operation(setup_calculations):
    """Test find calculation filterd by operation"""
    add_ops = Calculations.find_by_op("add")
    assert len(add_ops) == 1, "Did not find the correct number of add calculations"
    sub_ops = Calculations.find_by_op("subtract")
    assert len(sub_ops) == 1, "Did not find correct number of subtract calculations"

def test_get_latest_with_empty_history():
    """Test geting latest calculation with empty history"""
    Calculations.clear_history()
    assert Calculations.get_latest() is None, "Expected None for latest calculation with empty history"
