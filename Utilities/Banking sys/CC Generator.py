
import random
from datetime import datetime as dt


class CreditCardGenerator:
    def __init__(self):
        self.__visa_prefix = [4]
        self.__mastercard_prefix = [51, 52, 53, 54, 55]
        self.__amex_prefix = [34, 37]
        self.__discover_prefix = [6011]
        self.__credit_card_number = ""
        self.__cvv = ""
        self.__expiration_date = ""
        self.__card_issuer = ""
        self.__cardholder_name = ""

    def __generate_cc_number(self, prefix_list, length):
        try:
            cc_number = random.choice(prefix_list)

            while len(str(cc_number)) < (length - 1):
                cc_number = cc_number * 10 + random.randint(0,9)

            check_digit = self.__luhn_algorithm(cc_number)
            cc_number = cc_number * 10 + check_digit

            return str(cc_number)

        except Exception as e:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")

    def __luhn_algorithm(self, cc_number):
        try:
            cc_digits = [int(d) for d in str(cc_number)]
            check_sum = 0
            parity = len(cc_digits) % 2

            for i, digit in enumerate(cc_digits):
                if i % 2 == parity:
                    digit *= 2
                    if digit > 9:
                        digit -= 9
                check_sum += digit

            return (10 - check_sum % 10) % 10

        except Exception as e:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")

    def __generate_cvv(self, card_type):
        try:
            if card_type.lower() == "american express":
                return str(random.randint(1000,9999))
            else:
                return str(random.randint(100,999))

        except Exception as e:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")

    def __generate_expiry_date(self):
        try:
            month = str(random.randint(1,12)).zfill(2)
            year = str(random.randint(22,25))

            return month + "/" + year

        except Exception as e:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")

    def __validate_expiration_date(self, month, year):
        try:
            current_year = dt.now().year % 100

            while int(year) < current_year:
                year = input("Invalid year. Please enter a valid year (YY): ")

            if int(year) == current_year:
                current_month = dt.now().month
                while int(month) < current_month:
                    month = input("Invalid month. Please enter a valid month (MM): ")

            return (month.zfill(2), year)

        except Exception as e:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")

    def __validate_card(self, card_type):
        if card_type.lower() == "visa" or card_type == "1":
            self.__credit_card_number = self.__generate_cc_number(self.__visa_prefix, 16)
            self.__cvv = self.__generate_cvv(card_type)
            self.__card_issuer = "Visa"

        elif card_type.lower() == "mastercard" or card_type == "2":
            self.__credit_card_number = self.__generate_cc_number(self.__mastercard_prefix, 16)
            self.__cvv = self.__generate_cvv(card_type)
            self.__card_issuer = "Mastercard"

        elif card_type.lower() == "american express" or card_type == "3":
            self.__credit_card_number = self.__generate_cc_number(self.__amex_prefix, 15)
            self.__cvv = self.__generate_cvv(card_type)
            self.__card_issuer = "American Express"

        elif card_type.lower() == "discover" or card_type == "4":
            self.__credit_card_number = self.__generate_cc_number(self.__discover_prefix, 16)
            self.__cvv = self.__generate_cvv(card_type)
            self.__card_issuer = "Discover"

        elif card_type == "0" or card_type == "":
            exit(0)

        else:
            print("Invalid Card Type")
            return

    def __cc_format(self):
        return ' '.join([self.__credit_card_number[i:i+4] for i in range(0, len(self.__credit_card_number), 4)])

    def __run(self):
        try:
            print("\n1. Visa\n2. Mastercard\n3. American Express\n4. Discover")
            card_type = input("\nCard type: ")
            self.__validate_card(card_type)


            custom_exp_date = input("\nSet the expiration date? (y/n): ")
            if custom_exp_date.lower() == "y":
                month = input("Set expiration Month (MM): ")
                year = input("Set expiration Year (YY): ")
                month, year = self.__validate_expiration_date(month, year)
                self.__expiration_date = month + "/" + year
            else:
                self.__expiration_date = self.__generate_expiry_date()


            custom_card_issuer = input("Set the Card Issuer? (y/n): ")
            if custom_card_issuer.lower() == "y":
                self.__card_issuer = input("Card Issuer: ")


            custom_cardholder_name = input("Specify the Cardholder Name? (y/n): ")
            if custom_cardholder_name.lower() == "y":
                self.__cardholder_name = input("Cardholder Name: ")

            print(f"\nCredit Card Number: {self.__cc_format()}")
            print(f"Expiration Date: {self.__expiration_date}")
            print(f"CVV: {self.__cvv}")
            print(f"Card Issuer: {self.__card_issuer}")

            if self.__cardholder_name:
                print(f"Cardholder's Name: {self.__cardholder_name}")

        except Exception as e:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")

    def run(self):
        self.__run()


if __name__ == "__main__":
    cc_gen = CreditCardGenerator()
    cc_gen.run()