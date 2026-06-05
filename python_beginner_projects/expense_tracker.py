"""
Project Title: Expense Tracker

Project Description:
Advanced beginner project to track expenses. Supports adding expenses,
viewing all expenses, calculating total expenses, and category-wise tracking.
Uses a list of dictionaries to store expense entries.

Sample Flow:
1 Add Expense: amount, category, description
2 View Expenses
3 View Total Expenses
4 View Category Summary
5 Exit

Concepts Used:
- Lists and dictionaries, date/time, aggregation, input validation, exception handling

Run:
python expense_tracker.py
"""

from datetime import datetime


def get_positive_float(prompt):
    """Prompt user for a positive float with validation."""
    while True:
        try:
            value = input(prompt).strip()
            amt = float(value)
            if amt <= 0:
                print("Amount must be greater than zero. Try again.")
                continue
            return amt
        except ValueError:
            print("Invalid amount. Enter a numeric value.")


def get_nonempty(prompt):
    while True:
        v = input(prompt).strip()
        if v:
            return v
        print("Input cannot be empty. Try again.")


def add_expense(expenses):
    """Add a new expense entry to the expenses list."""
    amount = get_positive_float("Enter expense amount: ")
    category = get_nonempty("Enter category (e.g., Food, Transport): ")
    description = input("Enter description (optional): ").strip()
    date_str = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
    if date_str:
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Using today's date instead.")
            date = datetime.now().date()
    else:
        date = datetime.now().date()

    entry = {
        'amount': amount,
        'category': category,
        'description': description,
        'date': str(date),
    }
    expenses.append(entry)
    print("Expense added.")


def view_expenses(expenses):
    """Display all expenses in a table-like format."""
    if not expenses:
        print("No expenses recorded.")
        return
    print("\nExpenses:")
    for i, e in enumerate(expenses, start=1):
        print(f"{i}. {e['date']} | {e['category']} | ${e['amount']:.2f} | {e['description']}")


def total_expenses(expenses):
    """Return total amount spent."""
    total = sum(e['amount'] for e in expenses)
    print(f"Total expenses: ${total:.2f}")
    return total


def category_summary(expenses):
    """Print total spent per category and count of items."""
    if not expenses:
        print("No expenses to summarize.")
        return
    summary = {}
    for e in expenses:
        cat = e['category']
        summary.setdefault(cat, {'total': 0.0, 'count': 0})
        summary[cat]['total'] += e['amount']
        summary[cat]['count'] += 1

    print("\nCategory Summary:")
    for cat, info in summary.items():
        print(f"{cat}: ${info['total']:.2f} across {info['count']} items")


def delete_expense(expenses):
    """Delete an expense by its index shown to the user."""
    if not expenses:
        print("No expenses to delete.")
        return
    view_expenses(expenses)
    while True:
        try:
            idx = int(input("Enter expense number to delete (or 0 to cancel): ").strip())
            if idx == 0:
                print("Deletion cancelled.")
                return
            if 1 <= idx <= len(expenses):
                removed = expenses.pop(idx - 1)
                print(f"Removed: {removed['category']} ${removed['amount']:.2f} on {removed['date']}")
                return
            print("Invalid number. Try again.")
        except ValueError:
            print("Please enter a valid integer.")


def main():
    print("Expense Tracker")
    expenses = []

    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Expenses")
        print("4. View Category Summary")
        print("5. Delete Expense")
        print("6. Exit")

        choice = input("Enter choice (1-6): ").strip()
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            total_expenses(expenses)
        elif choice == '4':
            category_summary(expenses)
        elif choice == '5':
            delete_expense(expenses)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Please select a valid option.")


if __name__ == "__main__":
    main()
