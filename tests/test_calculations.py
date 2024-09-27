'''Operations Test'''
from calculator.operations import add, multiply, subtract, divide

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
    