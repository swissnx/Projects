
import math
import re

class PasswordChecker:
    def __init__(self):
        self.__password = None

    def __check_length(self):
        return len(self.__password) >= 8

    def __check_uppercase(self):
        return any(c.isupper() for c in self.__password)

    def __check_lowercase(self):
        return any(c.islower() for c in self.__password)

    def __check_digits(self):
        return any(c.isdigit() for c in self.__password)

    def __check_special(self):
        special_characters = "!@#$%^&*()-+"
        return any(c in special_characters for c in self.__password)

    def __check_non_alphanumeric(self):
        return any(not c.isalnum() for c in self.__password)

    def __check_consecutive_characters(self):
        return not re.search(r'(.)\1\1', self.__password)

    def __calculate_entropy(self):
        character_space = 0
        if any(c.islower() for c in self.__password):
            character_space += 26
        if any(c.isupper() for c in self.__password):
            character_space += 26
        if any(c.isdigit() for c in self.__password):
            character_space += 10
        if any(not c.isalnum() for c in self.__password):
            character_space += 32

        password_length = len(self.__password)
        entropy = math.log2(character_space ** password_length)

        return entropy

    @staticmethod
    def __format_time(seconds: float) -> str:
        if seconds < 60:
            return f"{seconds:.2f} seconds"
        elif seconds < 60 * 60:
            return f"{seconds / 60:.2f} minutes"
        elif seconds < 60 * 60 * 24:
            return f"{seconds / (60 * 60):.2f} hours"
        elif seconds < 60 * 60 * 24 * 365:
            return f"{seconds / (60 * 60 * 24):.2f} days"
        else:
            years = seconds / (60 * 60 * 24 * 365)
            if years < 1:
                return f"{years * 365:.2f} days"
            else:
                return f"{years:.2f} years"

    def __brute_force_duration(self):
        return (2 ** self.__calculate_entropy) / (10 ** 10)

    def __run(self):
        try:
            self.__password = input("Enter password: ")

            if self.__check_length() and self.__check_uppercase() and self.__check_lowercase() and self.__check_digits() and \
            self.__check_special() and self.__check_non_alphanumeric() and self.__check_consecutive_characters():
                print("Password is strong.")
            
            entropy = self.__calculate_entropy()
            print(f"Entropy: {entropy:.2f} bits")
            
            formatted_bf_duration = PasswordChecker.__format_time(self.__brute_force_duration())
            print(f"Estimated time to crack password using brute-force attack: {formatted_bf_duration}")
        
        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"
    
    def run(self):
        return self.__run()


if __name__ == "__main__":
    checker = PasswordChecker()
    checker.run()
