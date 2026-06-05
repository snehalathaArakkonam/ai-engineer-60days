"""
Project Title: Grade Calculator

Project Description:
Accept marks for 5 subjects, calculate total, percentage and assign a grade based
on the percentage.

Sample Input:
Enter marks for subject 1: 80
... (5 subjects)

Sample Output:
Total: 420
Percentage: 84.0%
Grade: A

Concepts Used:
- Lists, loops, input validation, arithmetic operations, functions

Run:
python grade_calculator.py
"""


def get_mark(index):
    """Prompt the user for a single mark (0-100) and validate it."""
    while True:
        try:
            value = input(f"Enter marks for subject {index} (0-100): ").strip()
            mark = float(value)
            if mark < 0 or mark > 100:
                print("Marks should be between 0 and 100. Try again.")
                continue
            return mark
        except ValueError:
            print("Invalid input. Please enter a numeric value for marks.")


def calculate_grade(percentage):
    """Return a letter grade based on percentage."""
    if percentage >= 90:
        return 'A+'
    if percentage >= 80:
        return 'A'
    if percentage >= 70:
        return 'B+'
    if percentage >= 60:
        return 'B'
    if percentage >= 50:
        return 'C'
    return 'F'


def main():
    print("Grade Calculator - Enter marks for 5 subjects")
    marks = []
    for i in range(1, 6):
        mark = get_mark(i)
        marks.append(mark)

    total = sum(marks)
    max_total = 5 * 100
    percentage = (total / max_total) * 100
    grade = calculate_grade(percentage)

    print(f"\nTotal: {total}")
    print(f"Percentage: {round(percentage, 2)}%")
    print(f"Grade: {grade}")


if __name__ == "__main__":
    main()
