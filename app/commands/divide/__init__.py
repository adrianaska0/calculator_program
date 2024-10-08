from app.commands import Command
from calculator import Calculator

class DivideCommand(Command):
    def execute(self, a, b):
        print(Calculator.div(a, b))
