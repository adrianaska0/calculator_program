from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

class Calculator:
	@staticmethod
	def add(a,b):
		calculation = Calculation(a, b, add)
		return calculation.get_res()
	@staticmethod
	def sub(a,b):
		calculation = Calculation(a, b, subtract)
		return calculation.get_res()
	@staticmethod
	def mult(a,b):
		calculation = Calculation(a, b, multiply)
		return calculation.get_res()
	@staticmethod
	def div(a,b):
		calculation = Calculation(a, b, divide)
		return calculation.get_res()