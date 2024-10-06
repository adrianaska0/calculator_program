""" Test Accept User Input """
import pytest
from main import calculate_and_log

@pytest.mark.parametrize("a_val, b_val, op_val, expected_val", [
    ("7", "6", 'add', "The result of 7 add 6 is equal to 13"),
    ("15", "11", 'subtract', "The result of 15 subtract 11 is equal to 4"),
    ("3", "3", 'multiply', "The result of 3 multiply 3 is equal to 9"),
    ("21", "7", 'divide', "The result of 21 divide 7 is equal to 3"),
    ("1", "0", 'divide', "An error occured: Cannot divide by zero"),
    ("9", "3", 'plex', "Unknown operation: plex"),
    ("a", "5", 'multiply', "Invalid operand input: a or 5 is not a valid number."),
    ("5", "b", 'subtract', "Invalid operand input: 5 or b is not a valid number.")
])
def test_calculate_and_log(a_val, b_val, op_val, expected_val, capsys):
    """Test Calculate and Log from main"""
    calculate_and_log(a_val, b_val, op_val)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_val
    