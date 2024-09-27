from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide
from calculator.calculations import Calculations
from decimal import Decimal
from typing import Callable

class Calculator:
	@staticmethod
	def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
		c = Calculation.create(a, b, operation) #create object
		Calculations.add_calculation(c) #add to history
		return c.perform()

	@staticmethod
	def add(a: Decimal, b: Decimal) -> Decimal:
		return Calculator._perform_operation(a, b, add)

	@staticmethod
	def sub(a: Decimal, b: Decimal) -> Decimal:
		return Calculator._perform_operation(a, b, subtract)

	@staticmethod
	def mult(a: Decimal, b: Decimal) -> Decimal:
		return Calculator._perform_operation(a, b, multiply)

	@staticmethod
	def div(a: Decimal, b: Decimal) -> Decimal:
		return Calculator._perform_operation(a, b, divide)