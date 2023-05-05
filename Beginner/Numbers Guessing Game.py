
import random

number = random.randrange(0, 10)
max_attempts = 5
attempts = 0

print(f"Guess the number between 1-10. You have {max_attempts} attempts.")
while attempts < max_attempts:
    try:
        guess = int(input("\nEnter your guess: "))
    except ValueError:
        print("\nInvalid input. Please enter a valid number.\n")
        continue

    attempts += 1
    if guess < number:
        print("Too low, try again.")
    elif guess > number:
        print("Too high, try again.")
    else:
        print(f"\nCongratz! You guessed it right in {attempts} attempts!")
        break
else:
    print(f"\nSorry, you ran out of attempts. The correct number was {number}.")
