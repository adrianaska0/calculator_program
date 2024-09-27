'''Calculator Test'''
from calculator import Calculator

def test_addition():
    assert Calculator.add(3,3) == 6

def test_subtraction():
    assert Calculator.sub(3,3) == 0

def test_multiply():
    assert Calculator.mult(3,3) == 9

def test_divide():
    assert Calculator.div(3,3) == 1