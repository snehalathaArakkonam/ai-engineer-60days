"""
Project Title: Number Guessing Game

Project Description:
Computer picks a random number and the user keeps guessing until they find it.
The program counts attempts and validates user input.

Sample Input/Output (example):
Guess the number between 1 and 100: 50
Too low. Try again.
Guess: 75
Too high. Try again.
Guess: 63
Correct! Attempts: 3

Concepts Used:
- Random number generation, loops, input validation

Run:
python number_guessing_game.py
"""

import random


def get_guess(prompt, low, high):
    """Get an integer guess from the user within range [low, high]."""
    while True:
        try:
            value = input(prompt).strip()
            guess = int(value)
            if guess < low or guess > high:
                print(f"Please guess a number between {low} and {high}.")
                continue
            return guess
        except ValueError:
            print("Invalid input. Enter an integer.")


def main():
    print("Number Guessing Game")
    low, high = 1, 100
    target = random.randint(low, high)
    attempts = 0

    print(f"Guess the number between {low} and {high}.")

    while True:
        guess = get_guess("Your guess: ", low, high)
        attempts += 1

        if guess < target:
            print("Too low. Try again.")
        elif guess > target:
            print("Too high. Try again.")
        else:
            print(f"Correct! You found the number in {attempts} attempts.")
            break


if __name__ == "__main__":
    main()
