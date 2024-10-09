import pytest
from decimal import Decimal
from unittest.mock import MagicMock, create_autospec
from app.commands import Command, CommandHandler

class TestCommand(Command):
    def execute(self, a, b):
        print(a * b)


def test_register_command():
    command_handler = CommandHandler()
    command_handler.register_command("test", TestCommand())
    assert "test" in command_handler.commands, "Command not in commands"

def test_execute_command(capfd):
    command_handler = CommandHandler()
    command_handler.register_command("test", TestCommand())
    command_handler.execute_command("test", Decimal('3'), Decimal('12'))
    out, err = capfd.readouterr()
    assert out == "36\n", "The answer should be 36."

# def test_execute(capfd):
#     command = TestCommand()
#     command.execute(Decimal('2'), Decimal('3'))
#     out, err = capfd.readouterr()
#     assert out == "6\n", "The answer should be 6"