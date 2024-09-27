from decimal import decimal

def add(a: Decimal, b: Decimal) -> Decimal:
    return a + b

def subtract(a: Decimal, b:Decimal) -> Decimal:
    return a - b

def multiply(a: Decimal, b:Decimal) -> Decimal:
    return a * b

def divide(a: Decimal, b:Decimal) -> Decimal:
    if b == 0:
        raise ValueError("Cannot divde by zero")
    return a / b