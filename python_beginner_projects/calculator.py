"""
Project Title: Simple Calculator

Project Description:
A beginner-friendly terminal calculator that supports addition, subtraction,
multiplication and division. The program is menu-driven and validates user input.

Sample Input:
1 (for Addition)
Enter first number: 5
Enter second number: 3

Sample Output:
Result: 8.0

Concepts Used:
- Variables, functions, input/output, control flow, loops
- Exception handling with try-except
- Input validation

Run:
python calculator.py
"""

def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return the division a / b. Raise ValueError for division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def get_number(prompt):
    """Prompt the user and return a float. Keeps asking until valid."""
    while True:
        try:
            value = input(prompt).strip()
            # Allow numbers like 5, 5.0, .5, -3
            number = float(value)
            return number
        except ValueError:
            print("Invalid number. Please enter a valid numeric value.")


def main():
    """Main menu loop for the calculator."""
    print("Simple Calculator - Menu")
    menu = (
        "1. Addition",
        "2. Subtraction",
        "3. Multiplication",
        "4. Division",
        "5. Exit",
    )

    while True:
        print("\nChoose an option:")
        for item in menu:
            print(item)

        choice = input("Enter choice (1-5): ").strip()

        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break

        if choice not in {'1', '2', '3', '4'}:
            print("Please enter a valid option between 1 and 5.")
            continue

        # Get two numbers safely
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        try:
            if choice == '1':
                result = add(num1, num2)
            elif choice == '2':
                result = subtract(num1, num2)
            elif choice == '3':
                result = multiply(num1, num2)
            elif choice == '4':
                result = divide(num1, num2)

            print(f"Result: {result}")

        except Exception as exc:
            # Catch any unexpected error (e.g., division by zero)
            print(f"Error: {exc}")


if __name__ == "__main__":
    main()
