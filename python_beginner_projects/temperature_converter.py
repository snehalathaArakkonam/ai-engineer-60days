"""
Project Title: Temperature Converter

Project Description:
Convert temperatures between Celsius and Fahrenheit. The program is menu-driven
and validates input.

Sample Input:
1 (for Celsius to Fahrenheit)
Enter temperature in Celsius: 0

Sample Output:
0.0°C => 32.0°F

Concepts Used:
- Functions, menu-driven programs, input validation, exception handling

Run:
python temperature_converter.py
"""


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def get_temperature(prompt):
    """Get a float temperature from user with validation."""
    while True:
        try:
            value = input(prompt).strip()
            temp = float(value)
            return temp
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")


def main():
    print("Temperature Converter")

    while True:
        print("\nMenu:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Exit")

        choice = input("Enter choice (1-3): ").strip()
        if choice == '3':
            print("Goodbye!")
            break

        if choice == '1':
            c = get_temperature("Enter temperature in Celsius: ")
            f = celsius_to_fahrenheit(c)
            print(f"{c}°C => {round(f, 2)}°F")

        elif choice == '2':
            f = get_temperature("Enter temperature in Fahrenheit: ")
            c = fahrenheit_to_celsius(f)
            print(f"{f}°F => {round(c, 2)}°C")

        else:
            print("Please enter a valid option (1-3).")


if __name__ == "__main__":
    main()
