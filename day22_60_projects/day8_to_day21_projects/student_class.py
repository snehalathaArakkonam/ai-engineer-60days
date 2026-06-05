"""
Project Title: Student Class (OOP Basics)

Project Description:
Simple demonstration of Object-Oriented Programming. Defines a `Student` class
with constructor, methods to add marks, compute average and display a summary.

Concepts Used:
- Classes and objects
- Constructor (`__init__`)
- Instance methods and encapsulation
- Basic input/output

Sample Input:
Enter student name: Alice
Enter roll number: 1
Enter marks for 3 subjects (comma separated): 80,90,75

Sample Output:
Student Summary for Alice (Roll: 1)
Marks: [80.0, 90.0, 75.0]
Average: 81.67

Run:
python student_class.py
"""

from typing import List


class Student:
    """A simple Student class to hold student data and compute statistics."""

    def __init__(self, name: str, roll: int, marks: List[float] = None):
        """Initialize a Student with name, roll and optional marks list."""
        self.name = name
        self.roll = roll
        # Use empty list if marks is None to avoid shared mutable default
        self.marks = marks[:] if marks else []

    def add_mark(self, mark: float):
        """Add a single numeric mark to the student's record."""
        try:
            mark = float(mark)
        except ValueError:
            raise ValueError("Mark must be a number")
        if mark < 0 or mark > 100:
            raise ValueError("Mark must be between 0 and 100")
        self.marks.append(mark)

    def average(self) -> float:
        """Return the average of marks, or 0.0 if no marks are present."""
        if not self.marks:
            return 0.0
        return sum(self.marks) / len(self.marks)

    def summary(self) -> str:
        """Return a formatted summary string for the student."""
        avg = self.average()
        marks_str = ', '.join(f"{m:.1f}" for m in self.marks)
        return (
            f"Student Summary for {self.name} (Roll: {self.roll})\n"
            f"Marks: [{marks_str}]\n"
            f"Average: {avg:.2f}"
        )


def parse_marks(input_str: str) -> List[float]:
    """Parse comma-separated marks from user input into a list of floats."""
    parts = [p.strip() for p in input_str.split(',') if p.strip()]
    marks = []
    for p in parts:
        try:
            val = float(p)
        except ValueError:
            raise ValueError(f"Invalid mark: {p}")
        if val < 0 or val > 100:
            raise ValueError(f"Mark out of range: {val}")
        marks.append(val)
    return marks


def main():
    print("Student Class Demo")
    try:
        name = input("Enter student name: ").strip()
        roll = int(input("Enter roll number: ").strip())
        marks_input = input("Enter marks for subjects (comma separated): ").strip()
        marks = parse_marks(marks_input) if marks_input else []

        student = Student(name=name, roll=roll, marks=marks)

        print('\n' + student.summary())

    except Exception as exc:
        print(f"Error: {exc}")


if __name__ == '__main__':
    main()
