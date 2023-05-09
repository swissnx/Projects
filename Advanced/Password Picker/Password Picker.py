
# A password picker is an app that generates strong passwords using words, numbers and symbols.

import secrets
import string
import time


def generate_password(adjectives: list, nouns: list, num_special_chars: int) -> str:
    adjective = secrets.choice(adjectives)
    noun = secrets.choice(nouns)
    number = str(secrets.randbelow(1_000_000))
    special_chars = ''.join([secrets.choice(string.punctuation) for _ in range(num_special_chars)])

    password_elements = [adjective, noun, number, special_chars]
    secrets.SystemRandom().shuffle(password_elements)

    password = ''.join(password_elements)
    return password


def pass_picker():
    print("✵✵✵ Welcome to Password Picker ✵✵✵")

    with open('adjectives.txt', 'r') as adj:  # Loading adjectives and nouns from a file or an API
        adjectives = adj.read().splitlines()

    with open('nouns.txt', 'r') as noun:
        nouns = noun.read().splitlines()

    password = generate_password(adjectives, nouns, 5)  # with num here indicate how many special chars to add
    time.sleep(1)
    print(f"\nYour Password is: \u001b[38;5;57m{password}\u001b[0m")

    while True:
        try:
            response = input("\nWould you like another password? (y/n): ")
            if response.upper() not in ['Y', 'N']:
                raise ValueError("Invalid response. Please enter Y or N.")
        except ValueError as e:
            print(e)
            continue
        if response.upper() == 'N':
            break

        password = generate_password(adjectives, nouns, 5)
        time.sleep(1)
        print(f"\nYour Password is: \u001b[38;5;57m{password}\u001b[0m")

    print("\nThank you for using Password Picker. Goodbye!")


if __name__ == '__main__':
    pass_picker()