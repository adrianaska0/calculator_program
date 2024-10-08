import sys
from app.commands import Command
from calculator import Calculator

class AddCommand(Command):
    def execute(self, a, b):
        print(Calculator.add(a, b))
