"""
Project Title: Calculator Using Functions (Modular)

Project Description:
Calculator implemented with separate functions for each operation to demonstrate
modular coding style and reusability.

Sample Input:
Select operation: add
Enter first number: 4
Enter second number: 2

Sample Output:
Result: 6.0

Concepts Used:
- Functions, modular design, exception handling, input validation

Run:
python calculator_functions.py
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def get_float(prompt):
    """Get a float from user with validation."""
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Please enter a valid number.")


def main():
    print("Calculator (Functions Demonstration)")
    operations = {
        'add': add,
        'sub': subtract,
        'mul': multiply,
        'div': divide,
    }

    while True:
        print("\nAvailable operations: add, sub, mul, div, exit")
        op = input("Select operation: ").strip().lower()
        if op == 'exit':
            print("Goodbye!")
            break
        if op not in operations:
            print("Unsupported operation. Try again.")
            continue

        a = get_float("Enter first number: ")
        b = get_float("Enter second number: ")

        try:
            func = operations[op]
            result = func(a, b)
            print(f"Result: {result}")
        except Exception as exc:
            print(f"Error: {exc}")


if __name__ == "__main__":
    main()
