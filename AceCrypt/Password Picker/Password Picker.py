
# A password picker is an app that generates strong passwords using words, numbers and symbols.

import secrets
import string
import time


class PasswordPicker:
    def __init__(self):
        self.__adjectives = []
        self.__nouns = []
        self.__load_words()
    
    def __load_words(self):
        with open('adjectives.txt', 'r') as adj:
            self.__adjectives = adj.read().splitlines()

        with open('nouns.txt', 'r') as noun:
            self.__nouns = noun.read().splitlines()

    def load_words(self):
        return self.__load_words()

    def __generate_password(self, num_special_chars: int) -> str:
        adjective = secrets.choice(self.__adjectives)
        noun = secrets.choice(self.__nouns)
        number = str(secrets.randbelow(1_000_000))
        special_chars = ''.join([secrets.choice(string.punctuation) for _ in range(num_special_chars)])
        password_elements = [adjective, noun, number, special_chars]
        secrets.SystemRandom().shuffle(password_elements)
        password = ''.join(password_elements)
        return password

    def generate_password(self, num_special_chars: int) -> str:
        return self.__generate_password(num_special_chars)

    def __run(self):
        print("✵✵✵ Welcome to Password Picker ✵✵✵")
        password = self.__generate_password(5)
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
            password = self.__generate_password(5)
            time.sleep(1)
            print(f"\nYour Password is: \u001b[38;5;57m{password}\u001b[0m")
        print("\nThank you for using Password Picker. Goodbye!")

    def run(self):
        return self.__run()


if __name__ == "__main__":
    picker = PasswordPicker()
    picker.run()
