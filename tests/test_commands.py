import pytest
from app import App
from decimal import Decimal
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand
from app.commands.menu import MenuCommand

def test_add_command(capfd):
    '''Test add command'''
    command = AddCommand()
    command.execute(Decimal('3'), Decimal('10'))
    out, err = capfd.readouterr()
    assert out == "13\n", "The AddCommand should print 13."
