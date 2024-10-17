from app.commands import Command
from calculator import Calculator
import logging

class DivideCommand(Command):
    def execute(self, a, b):
        logging.info("Executing divide command.")
        print(Calculator.div(a, b))
