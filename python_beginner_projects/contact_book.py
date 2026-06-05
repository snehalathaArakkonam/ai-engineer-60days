"""
Project Title: Contact Book

Project Description:
Simple contact manager using a dictionary to store contact information.
Supports add, view, search and delete operations.

Sample Flow:
1 Add Contact: Name, Phone, Email
2 View Contacts
3 Search Contact by name
4 Delete Contact

Concepts Used:
- Dictionaries, input validation, string handling, loops

Run:
python contact_book.py
"""


def get_nonempty(prompt):
    while True:
        val = input(prompt).strip()
        if val:
            return val
        print("Input cannot be empty. Try again.")


def add_contact(contacts):
    name = get_nonempty("Enter contact name: ")
    phone = get_nonempty("Enter phone number: ")
    email = input("Enter email (optional): ").strip()
    contacts[name] = {'phone': phone, 'email': email}
    print(f"Contact '{name}' added/updated.")


def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return
    print("\nContacts:")
    for name, info in contacts.items():
        email = info.get('email', '')
        print(f"Name: {name} | Phone: {info['phone']} | Email: {email}")


def search_contact(contacts):
    q = get_nonempty("Enter name or substring to search: ").lower()
    matches = {n: i for n, i in contacts.items() if q in n.lower()}
    if not matches:
        print("No matching contacts found.")
        return
    print("Found:")
    for name, info in matches.items():
        print(f"Name: {name} | Phone: {info['phone']} | Email: {info.get('email','')}")


def delete_contact(contacts):
    name = get_nonempty("Enter exact name of contact to delete: ")
    if name in contacts:
        confirm = input(f"Delete contact '{name}'? (y/n): ").strip().lower()
        if confirm == 'y':
            contacts.pop(name)
            print("Contact deleted.")
        else:
            print("Deletion cancelled.")
    else:
        print("Contact not found.")


def main():
    print("Contact Book")
    contacts = {}
    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter choice (1-5): ").strip()
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Please enter a valid option.")


if __name__ == "__main__":
    main()
