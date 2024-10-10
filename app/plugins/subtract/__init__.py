from app.commands import Command
from calculator import Calculator

class SubtractCommand(Command):
    def execute(self, a, b):
        print(Calculator.sub(a, b))
