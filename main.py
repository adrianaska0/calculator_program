import sys
from calculator import Calculator
from decimal import Decimal, InvalidOperation

def calculate_and_log(a, b, op_name):
    op_mappings = {
        'add': Calculator.add,
        'subtract': Calculator.sub,
        'multiply': Calculator.mult,
        'divide': Calculator.div
    }

    try:
        a_decimal, b_decimal = map(Decimal, [a,b])
        result = op_mappings.get(op_name)
        if result:
            print(f"The result of {a} {op_name} {b} is equal to {result(a_decimal, b_decimal)}")
        else:
            print(f"Unknown operation: {op_name}")
    except InvalidOperation:
        print(f"Invalid operand input: {a} or {b} is not a valid number.")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except Exception as e:
        print(f"An error occured: {e}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python calculator_main.py <number1> <number2> <operation>")
        sys.exit(1)

    _, a, b, operation = sys.argv
    calculate_and_log(a, b, operation)

if __name__ == '__main__':
    main()
