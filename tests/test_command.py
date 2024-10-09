import pytest
from unittest.mock import MagicMock, create_autospec
from app.commands import Command, CommandHandler

class TestCommand(Command):
    def execute(self, a, b):
        return a * b

def test_register_command():
    command_handler = CommandHandler()
    command_handler.register_command("test", TestCommand())
    assert "test" in command_handler.commands