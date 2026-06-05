"""
Project Title: Multiplication Tables

Project Description:
User enters a number and the program displays its multiplication table from 1 to 10.

Sample Input:
Enter a number: 5

Sample Output:
5 x 1 = 5
...
5 x 10 = 50

Concepts Used:
- Loops, input validation, formatting output

Run:
python multiplication_tables.py
"""


def get_integer(prompt):
    """Prompt the user for an integer and validate it."""
    while True:
        try:
            value = input(prompt).strip()
            n = int(value)
            return n
        except ValueError:
            print("Invalid input. Please enter an integer.")


def main():
    print("Multiplication Table Generator")
    num = get_integer("Enter a number: ")
    print(f"\nMultiplication table for {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")


if __name__ == "__main__":
    main()
