"""
Project Title: ATM Simulator

Project Description:
Simple ATM simulator supporting checking balance, deposit, withdraw and exit.
Prevents negative balance and validates input.

Sample Input/Flow:
1 (Check balance)
2 (Deposit) 100
3 (Withdraw) 50

Sample Output:
Balance: $0.00
Deposited $100.00
Withdrew $50.00

Concepts Used:
- State management, input validation, exception handling, loops

Run:
python atm_simulator.py
"""


def get_positive_amount(prompt):
    """Prompt user for a positive float amount with validation."""
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


def main():
    print("ATM Simulator")
    balance = 0.0  # starting balance

    while True:
        print("\nMenu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter choice (1-4): ").strip()
        if choice == '1':
            print(f"Current balance: ${balance:.2f}")

        elif choice == '2':
            amount = get_positive_amount("Enter amount to deposit: ")
            balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${balance:.2f}")

        elif choice == '3':
            amount = get_positive_amount("Enter amount to withdraw: ")
            if amount > balance:
                print("Insufficient funds. Withdrawal cancelled.")
            else:
                balance -= amount
                print(f"Withdrew ${amount:.2f}. New balance: ${balance:.2f}")

        elif choice == '4':
            print("Thank you for using the ATM Simulator. Goodbye!")
            break

        else:
            print("Invalid choice. Please select an option between 1 and 4.")


if __name__ == "__main__":
    main()
