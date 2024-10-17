from app.commands import Command
from calculator import Calculator
import logging

class SubtractCommand(Command):
    def execute(self, a, b):
        logging.info("Executing subtract command.")
        print(Calculator.sub(a, b))
