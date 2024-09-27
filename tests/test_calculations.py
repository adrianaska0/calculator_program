'''Operations Test'''
from calculator.operations import add, multiply, subtract, divide

def test_add():
    assert add(3,3) == 6

def test_subtract():
    assert sub(3,3) == 0

def test_multiply():
    assert multiply (3,3) == 9

def test_divide():
    assert divide(3,3) == 1