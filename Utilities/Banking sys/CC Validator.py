
class CreditCardValidator:
    def __init__(self):
        self.__card_number = None
        self.__card_type = None

    def __validate(self, card_number):
        try:
            self.__card_number = card_number.replace(" ", "")

            if not self.__is_valid_input():
                return False
            if not self.__is_valid_card_type():
                return False
            if not self.__passes_luhn_algorithm():
                return False
            return True

        except Exception as e:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")

    def validate(self, card_number):
        return self.__validate(card_number)

    def __is_valid_input(self):
        try:
            return all(char.isdigit() or char.isspace() for char in self.__card_number)

        except Exception as e:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")

    def is_valid_input(self):
        return self.__is_valid_input()

    def __is_valid_card_type(self):
        try:
            card_types = {"Visa": [4],
                          "Mastercard": [51, 52, 53, 54, 55],
                          "American Express": [34, 37]
                          }
            for card_type, prefixes in card_types.items():
                for prefix in prefixes:
                    if str(prefix) == self.__card_number[:len(str(prefix))]:
                        self.__card_type = card_type
                        return True
            return False

        except Exception as e:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")

    def is_valid_card_type(self):
        return self.__is_valid_card_type()

    def __passes_luhn_algorithm(self):
        try:
            card_number = [int(digit) for digit in self.__card_number]
            check_digit = card_number.pop(-1)
            card_number.reverse()

            for i in range(len(card_number)):
                if i % 2 == 0:
                    card_number[i] *= 2
                    if card_number[i] > 9:
                        card_number[i] -= 9

            total = sum(card_number) + check_digit

            return total % 10 == 0

        except Exception as e:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")
    
    def passes_luhn_algorithm(self):
        return self.__passes_luhn_algorithm()

    def __run(self):
        try:
            card_number = input("CC #: ")
            if self.__validate(card_number):
                print(f"Valid {self.__card_type} Credit Card Number.")
            else:
                print("Invalid Credit Card Number.")

        except Exception as e:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")

    def run(self):
        self.__run()


if __name__ == "__main__":
    validator = CreditCardValidator()
    validator.run()



# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ SQLite3 Database Added ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #

import sqlite3


class CreditCardValidator:
    def __init__(self):
        self.__card_number = None
        self.__card_type = None
        self.__db_connection = sqlite3.connect("credit_cards.db")
        self.__create_table()

    def __create_table(self):
        cursor = self.__db_connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS credit_cards (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                card_number TEXT NOT NULL,
                card_type TEXT NOT NULL,
                date_validated TEXT NOT NULL
            )
        """)
        self.__db_connection.commit()

    def create_table(self):
        return self.__create_table()

    def __store_card_info(self):
        cursor = self.__db_connection.cursor()
        cursor.execute("""
            INSERT INTO credit_cards (card_number, card_type, date_validated)
            VALUES (?, ?, datetime('now'))
        """, (self.__card_number, self.__card_type))
        self.__db_connection.commit()

    def store_card_info(self):
        return self.__store_card_info()

    def __validate(self, card_number):
        self.__card_number = card_number.replace(" ", "")
        if not self.__is_valid_input():
            return False
        if not self.__is_valid_card_type():
            return False
        if not self.__passes_luhn_algorithm():
            return False
        self.__store_card_info()
        return True

    def validate(self, card_number):
        return self.__validate(card_number)

    def __is_valid_input(self):
        return all(char.isdigit() or char.isspace() for char in self.__card_number)

    def is_valid_input(self):
        return self.__is_valid_input()

    def __is_valid_card_type(self):
        card_types = {
            "Visa": [4],
            "Mastercard": [51, 52, 53, 54, 55],
            "American Express": [34, 37]
        }
        for card_type, prefixes in card_types.items():
            for prefix in prefixes:
                if str(prefix) == self.__card_number[:len(str(prefix))]:
                    self.__card_type = card_type
                    return True
        return False

    def is_valid_card_type(self):
        return self.__is_valid_card_type()

    def __passes_luhn_algorithm(self):
        card_number = [int(digit) for digit in self.__card_number]
        check_digit = card_number.pop(-1)
        card_number.reverse()
        for i in range(len(card_number)):
            if i % 2 == 0:
                card_number[i] *= 2
                if card_number[i] > 9:
                    card_number[i] -= 9
        total = sum(card_number) + check_digit
        return total % 10 == 0

    def passes_luhn_algorithm(self):
        return self.__passes_luhn_algorithm()

    def __run(self):
        try:
            card_number = input("CC #: ")
            if self.__validate(card_number):
                print(f"Valid {self.__card_type} Credit Card Number.")
            else:
                print("Invalid Credit Card Number.")
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;196m{e}\u001b[0m")

    def run(self):
        self.__run()


if __name__ == "__main__":
    cc_validator = CreditCardValidator()
    cc_validator.run()
