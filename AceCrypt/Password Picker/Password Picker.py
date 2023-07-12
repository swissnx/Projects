
import secrets
import string
import time


class PasswordPicker:
    def __init__(self):
        self.__adjectives = []
        self.__nouns = []
        self.__load_words()
    
    def __load_words(self):
        try:
            with open('adjectives.txt', 'r') as adj:
                self.__adjectives = adj.read().splitlines()

            with open('nouns.txt', 'r') as noun:
                self.__nouns = noun.read().splitlines()

        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def load_words(self):
        return self.__load_words()

    def __generate_password(self, num_special_chars: int) -> str:
        try:
            adjective = secrets.choice(self.__adjectives)
            noun = secrets.choice(self.__nouns)
            number = str(secrets.randbelow(1_000_000))
            special_chars = ''.join([secrets.choice(string.punctuation) for _ in range(num_special_chars)])
            password_elements = [adjective, noun, number, special_chars]
            secrets.SystemRandom().shuffle(password_elements)
            password = ''.join(password_elements)

            return password
        
        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def generate_password(self, num_special_chars: int) -> str:
        return self.__generate_password(num_special_chars)

    def __run(self):
        try:
            print("✵✵✵ Welcome to Password Picker ✵✵✵")

            password = self.__generate_password(5)
            time.sleep(1)
            print(f"\nYour Password is: \u001b[38;5;57m{password}\u001b[0m")

            while True:
                try:
                    response = input("\nTry another one? (y/n): ")
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

        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def run(self):
        return self.__run()


if __name__ == "__main__":
    pass_picker = PasswordPicker()
    pass_picker.run()


# A password picker is an app that generates strong passwords using words, numbers and symbols.