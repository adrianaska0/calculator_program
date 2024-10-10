import pytest
from app import App
from decimal import Decimal
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand
from app.plugins.menu import MenuCommand
from app.commands import CommandHandler
from unittest.mock import MagicMock

def test_add_command(capfd):
    '''Test add command'''
    command = AddCommand()
    command.execute(Decimal('3'), Decimal('10'))
    out, err = capfd.readouterr()
    assert out == "13\n", "The AddCommand should print 13."

def test_subtract_command(capfd):
    '''Test subtract command'''
    command = SubtractCommand()
    command.execute(Decimal('10'), Decimal('3'))
    out, err = capfd.readouterr()
    assert out == "7\n", "The SubtractCommand should print 7."

def test_multiply_command(capfd):
    '''Test multiply command'''
    command = MultiplyCommand()
    command.execute(Decimal('4'), Decimal('5'))
    out, err = capfd.readouterr()
    assert out == "20\n", "The MultiplyCommand should print 20."

def test_divide_command(capfd):
    '''Test divide command'''
    command = DivideCommand()
    command.execute(Decimal('12'), Decimal('4'))
    out, err = capfd.readouterr()
    assert out == "3\n", "The DivideCommand should print 3."

def test_menu_command(capfd):
    '''Test menu command'''
    command_handler = CommandHandler()
    command_handler.register_command("add", MagicMock())
    command_handler.register_command("menu", MagicMock())
    command = MenuCommand(command_handler)
    command.execute(None, None)
    out, err = capfd.readouterr()
    assert "Available commands:" in out
    assert "- add" in out
    assert "- menu" in out

def test_divide_zero_command(capfd):
    '''Test divide by zero command'''
    command = DivideCommand()
    with pytest.raises(ValueError) as e:
        command.execute(Decimal('15'), Decimal('0'))
    assert str(e.value) == "Cannot divide by zero", "Should return cannot divide by zero"
    