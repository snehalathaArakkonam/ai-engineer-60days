"""
Project Title: Student Management System (In-memory)

Project Description:
Simple terminal-based system to add, view, search and delete student records.
Data is stored in-memory using a list of dictionaries. This is suitable for
beginner practice and demonstrates basic data structures and CRUD operations.

Sample Flow:
1 (Add Student) -> Enter name, age
2 (View Students)
3 (Search Student) -> search by ID or name
4 (Delete Student) -> provide ID

Concepts Used:
- Lists, dictionaries, functions, input validation, exception handling

Run:
python student_management_system.py
"""


def get_nonempty_string(prompt):
    """Prompt until a non-empty string is provided."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Try again.")


def get_int(prompt):
    """Prompt until a valid integer is provided."""
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Please enter a valid integer.")


def add_student(students, next_id):
    """Add a new student and return updated next_id."""
    name = get_nonempty_string("Enter student name: ")
    age = get_int("Enter student age: ")
    student = {'id': next_id, 'name': name, 'age': age}
    students.append(student)
    print(f"Student added with ID {next_id}.")
    return next_id + 1


def view_students(students):
    """Print all students in a formatted way."""
    if not students:
        print("No students available.")
        return
    print("\nStudents:")
    for s in students:
        print(f"ID: {s['id']} | Name: {s['name']} | Age: {s['age']}")


def search_student(students):
    """Search by ID or name substring and show matches."""
    query = get_nonempty_string("Enter student ID or name to search: ")
    found = []
    # Try interpret as ID
    try:
        qid = int(query)
        found = [s for s in students if s['id'] == qid]
    except ValueError:
        qlower = query.lower()
        found = [s for s in students if qlower in s['name'].lower()]

    if not found:
        print("No matching students found.")
        return
    print("Found:")
    for s in found:
        print(f"ID: {s['id']} | Name: {s['name']} | Age: {s['age']}")


def delete_student(students):
    """Delete a student by ID if exists."""
    sid = get_int("Enter student ID to delete: ")
    for i, s in enumerate(students):
        if s['id'] == sid:
            confirm = input(f"Delete {s['name']} (ID {sid})? (y/n): ").strip().lower()
            if confirm == 'y':
                students.pop(i)
                print("Student deleted.")
            else:
                print("Deletion cancelled.")
            return
    print("Student with given ID not found.")


def main():
    print("Student Management System")
    students = []
    next_id = 1

    while True:
        print("\nMenu:")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice (1-5): ").strip()
        if choice == '1':
            next_id = add_student(students, next_id)
        elif choice == '2':
            view_students(students)
        elif choice == '3':
            search_student(students)
        elif choice == '4':
            delete_student(students)
        elif choice == '5':
            print("Exiting Student Management System.")
            break
        else:
            print("Please choose a valid option (1-5).")


if __name__ == "__main__":
    main()
