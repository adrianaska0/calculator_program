from abc import ABC, abstractmethod
import logging

class Command(ABC):
    @abstractmethod
    def execute(self, a, b):
        self.a = a
        self.b = b
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command
    
    def execute_command(self, command_name: str, a, b):
        try:
            self.commands[command_name].execute(a, b)
        except KeyError:
            print(f"No such command: {command_name}")
            logging.error(f"No such command: {command_name}")