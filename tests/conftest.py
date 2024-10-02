import pytest
from decimal import Decimal
from faker import faker
from calculator.operations import add, subtract, multiply, divide

fake = Faker()

def generate_test_data(num_records):
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }

    for i in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        b = Decimal(fake.random_number(digits=2)) if i % 4 != 3 else Decimal(fake.random_number(digits=1))
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]