"""Calculator Test"""
from calculator import Calculator

def test_addition():
    """Test add function works"""
    assert Calculator.add(3,3) == 6

def test_subtraction():
    """Test sub function works"""
    assert Calculator.sub(3,3) == 0

def test_multiply():
    """Test mult function works"""
    assert Calculator.mult(3,3) == 9

def test_divide():
    """Test div function works"""
    assert Calculator.div(3,3) == 1
    