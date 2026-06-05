"""
Project Title: Robust Calculator (Exception Handling)

Project Description:
Calculator that handles invalid input and division by zero using try-except
blocks. Menu-driven and prevents crashes on bad input.

Concepts Used:
- try-except for error handling
- Functions and input validation

Sample Input/Flow:
Select operation: 1 (Addition)
Enter first number: a (invalid) -> prompts again

Sample Output:
Result: 5.0

Run:
python robust_calculator.py
"""


def get_number(prompt):
    """Prompt until a valid float is entered."""
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Invalid number. Please try again.")


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def main():
    print("Robust Calculator")
    menu = {
        '1': ('Addition', add),
        '2': ('Subtraction', subtract),
        '3': ('Multiplication', multiply),
        '4': ('Division', divide),
        '5': ('Exit', None)
    }

    while True:
        for k, v in menu.items():
            print(f"{k}. {v[0]}")
        choice = input("Choose an option: ").strip()
        if choice == '5':
            print('Goodbye!')
            break
        if choice not in menu:
            print('Invalid choice. Try again.')
            continue

        a = get_number('Enter first number: ')
        b = get_number('Enter second number: ')
        try:
            result = menu[choice][1](a, b)
            print(f"Result: {result}")
        except ZeroDivisionError as zde:
            print(f"Error: {zde}")
        except Exception as exc:
            print(f"An unexpected error occurred: {exc}")


if __name__ == '__main__':
    main()
