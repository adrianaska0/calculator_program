# pylint: disable= unused-variable, unused-import
"""Test command registration and execution"""
from decimal import Decimal
import pytest
from app.commands import Command, CommandHandler

class TestCommand(Command):
    """Command for Testing"""
    def execute(self, a, b):
        print(a * b)


def test_register_command():
    """Test command registration"""
    command_handler = CommandHandler()
    command_handler.register_command("test", TestCommand())
    assert "test" in command_handler.commands, "Command not in commands"

def test_execute_command(capfd):
    """Test command exection"""
    command_handler = CommandHandler()
    command_handler.register_command("test", TestCommand())
    command_handler.execute_command("test", Decimal('3'), Decimal('12'))
    out, err = capfd.readouterr()
    assert out == "36\n", "The answer should be 36."
