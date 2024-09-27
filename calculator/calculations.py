from decimal import Decimal
from typing import Callable, List

from calculator.calculation import Calculation

class Calculations:
    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        '''Add new calculation to history'''
        cls.history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        '''Get list of calculation history'''
        return cls.history

    @classmethod
    def clear_history(cls):
        '''Clear list of calculation history'''
        cls.history.clear()

    @classmethod
    def get_latest(cls) -> Calculation:
        '''Retrieve latest calculation. Return None if does not exist'''
        if cls.history:
            return cls.history[-1]
        return None

    @classmethod
    def find_by_op(cls, op_name: str) -> List[Calculation]:
        '''Retrieve list of calculations by operation'''
        return [c for c in cls.history if c.operation.__name__ == op_name]