"""
Project Title: Notes App (File Handling)

Project Description:
Simple terminal notes application that stores notes in a text file `notes.txt`.
Supports creating, viewing, appending and deleting notes.

Concepts Used:
- File I/O (read, write, append)
- Exception handling
- Basic menu-driven interface

Sample Input/Flow:
1 (Create Note) -> Enter note text
2 (View Notes)
3 (Append Note)
4 (Delete Notes)
5 (Exit)

Sample Output:
Note saved to notes.txt

Run:
python notes_app.py
"""

import os
from typing import List


NOTES_FILE = 'notes.txt'


def read_notes() -> List[str]:
    """Return the list of notes from NOTES_FILE. Create file if missing."""
    if not os.path.exists(NOTES_FILE):
        open(NOTES_FILE, 'a', encoding='utf-8').close()
        return []
    with open(NOTES_FILE, 'r', encoding='utf-8') as f:
        lines = [line.rstrip('\n') for line in f]
    return lines


def write_notes(notes: List[str]):
    """Overwrite the notes file with the provided list of notes."""
    with open(NOTES_FILE, 'w', encoding='utf-8') as f:
        for n in notes:
            f.write(n + '\n')


def append_note(note: str):
    """Append a single note to the file."""
    with open(NOTES_FILE, 'a', encoding='utf-8') as f:
        f.write(note + '\n')


def display_notes():
    notes = read_notes()
    if not notes:
        print("No notes found.")
        return
    print("\nNotes:")
    for i, n in enumerate(notes, start=1):
        print(f"{i}. {n}")


def delete_note_by_index(index: int):
    notes = read_notes()
    if 1 <= index <= len(notes):
        removed = notes.pop(index - 1)
        write_notes(notes)
        print(f"Deleted note: {removed}")
    else:
        print("Index out of range.")


def main():
    print("Notes App")
    while True:
        print('\nMenu:')
        print('1. Create Note (overwrite file)')
        print('2. View Notes')
        print('3. Append Note')
        print('4. Delete Note')
        print('5. Exit')

        choice = input('Enter choice (1-5): ').strip()
        try:
            if choice == '1':
                text = input('Enter note text (this will overwrite existing notes): ').strip()
                write_notes([text])
                print('Note saved to notes.txt')
            elif choice == '2':
                display_notes()
            elif choice == '3':
                text = input('Enter note to append: ').strip()
                append_note(text)
                print('Note appended.')
            elif choice == '4':
                display_notes()
                idx = input('Enter note number to delete (or press Enter to cancel): ').strip()
                if idx:
                    delete_note_by_index(int(idx))
            elif choice == '5':
                print('Goodbye!')
                break
            else:
                print('Please select a valid option.')
        except Exception as exc:
            print(f'Error: {exc}')


if __name__ == '__main__':
    main()
