'''Calculations Test'''

from decimal import Decimal
import pytest

from calculator.calculation import Calculation
from calculator.calculations import Calculations

from calculator.operations import add, multiply, subtract, divide

@pytest.fixture
def setup_calculations():
    Calculations.clear_history()
    Calculations.add_calculation(Calculation(Decimal('10'), Decimal('5'), add))
    Calculations.add_calculation(Calculation(Decimal('20'), Decimal('5'), subtract))

def test_add_calculation(setup_calculations):
    c = Calculation(Decimal('3'), Decimal('3'), add)
    Calculations.add_calculation(c)
    assert Calculations.get_latest() == calc, "Failed to add the calculation to history"

def test_get_history(setup_calculations):
    history = Calculations.get_history()
    assert len(history) == 2, "History does not have the expected number of calculations"

def test_clear_history(setup_calculations):
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0, "History was not cleared"

def test_get_latest(setup_calculations):
    latest = Calculations.get_latest()
    assert latest.a = Decimal('20') and latest.b = Decimal('5'), "Did not get correct latest calculation"

def test_find_by_operation(setup_calculations):
    add_ops = Calculations.find_by_operation("add")
    assert len(add_ops) == 1, "Did not find the correct number of add calculations"
    sub_ops = Calculations.find_by_operation("subtract")
    assert len(sub_ops) == 1, "Did not find correct number of subtract calculations"

def test_get_latest_with_empty_history():
    Calculations.clear_history()
    assert Calculations.get_latest() is None, "Expected None for latest calculation with empty history"
def test_add():
    '''Test addition function works'''
    assert add(3,3) == 6

def test_subtract():
    '''Test subtraction function works'''
    assert subtract(3,3) == 0

def test_multiply():
    '''Test multiplication function works'''
    assert multiply (3,3) == 9

def test_divide():
    '''Test division function works'''
    assert divide(3,3) == 1
