from app.commands import Command
from calculator import Calculator

class MultiplyCommand(Command):
    def execute(self, a, b):
        print(Calculator.mult(a, b))
