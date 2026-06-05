"""
Project Title: Age Calculator

Project Description:
User enters their birth year and the program calculates the current age.
Input is validated to prevent impossible years and non-numeric input.

Sample Input:
Enter birth year: 1990

Sample Output:
You are 36 years old.

Concepts Used:
- datetime for current year
- Input validation, exception handling

Run:
python age_calculator.py
"""

from datetime import datetime


def get_birth_year():
    """Prompt user for birth year and validate it.

    Returns:
        int: valid birth year
    """
    current_year = datetime.now().year
    while True:
        try:
            value = input("Enter birth year (e.g., 1990): ").strip()
            year = int(value)

            # Basic validation: reasonable birth year (e.g., between 1900 and current_year)
            if year < 1900:
                print("Birth year seems too old. Please enter a realistic year (>=1900).")
                continue
            if year > current_year:
                print("Birth year cannot be in the future. Please enter a valid year.")
                continue

            return year

        except ValueError:
            print("Invalid input. Please enter a numeric year like 1990.")


def calculate_age(birth_year):
    """Calculate age given birth_year using the current year."""
    today = datetime.now()
    age = today.year - birth_year
    return age


def main():
    print("Age Calculator")
    birth_year = get_birth_year()
    age = calculate_age(birth_year)
    print(f"You are {age} years old.")


if __name__ == "__main__":
    main()
