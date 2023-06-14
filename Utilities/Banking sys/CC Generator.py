
import random
from datetime import datetime

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

    def __generate_credit_card_number(self, prefix_list, length):
        cc_number = random.choice(prefix_list)
        while len(str(cc_number)) < (length - 1):
            cc_number = cc_number * 10 + random.randint(0,9)
        check_digit = self.__luhn_algorithm(cc_number)
        cc_number = cc_number * 10 + check_digit
        return str(cc_number)

    def __luhn_algorithm(self, cc_number):
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

    def __generate_cvv(self, card_type):
        if card_type.lower() == "american express":
            return str(random.randint(1000,9999))
        else:
            return str(random.randint(100,999))

    def __generate_expiration_date(self):
        month = str(random.randint(1,12)).zfill(2)
        year = str(random.randint(22,25))
        return month + "/" + year

    def __validate_expiration_date(self, month, year):
        current_year = datetime.now().year % 100
        while int(year) < current_year:
            year = input("Invalid year. Please enter a valid year (YY): ")
        if int(year) == current_year:
            current_month = datetime.now().month
            while int(month) < current_month:
                month = input("Invalid month. Please enter a valid month (MM): ")
        return (month.zfill(2), year)

    def __run(self):
        try:
            print("\nOptions:\n1. Visa\n2. Mastercard\n3. American Express\n4. Discover")
            card_type = input("\nCard type: ")
            if card_type.lower() == "visa" or card_type == "1":
                self.__credit_card_number = self.__generate_credit_card_number(self.__visa_prefix, 16)
                self.__cvv = self.__generate_cvv(card_type)
                self.__card_issuer = "Visa"
            elif card_type.lower() == "mastercard" or card_type == "2":
                self.__credit_card_number = self.__generate_credit_card_number(self.__mastercard_prefix, 16)
                self.__cvv = self.__generate_cvv(card_type)
                self.__card_issuer = "Mastercard"
            elif card_type.lower() == "american express" or card_type == "3":
                self.__credit_card_number = self.__generate_credit_card_number(self.__amex_prefix, 15)
                self.__cvv = self.__generate_cvv(card_type)
                self.__card_issuer = "American Express"
            elif card_type.lower() == "discover" or card_type == "4":
                self.__credit_card_number = self.__generate_credit_card_number(self.__discover_prefix, 16)
                self.__cvv = self.__generate_cvv(card_type)
                self.__card_issuer = "Discover"
            else:
                print("Invalid card type")
                return

            custom_exp_date = input("\nSet the expiration date? (y/n): ")
            if custom_exp_date.lower() == "y":
                month = input("Set expiration month (MM): ")
                year = input("Set expiration year (YY): ")
                month, year = self.__validate_expiration_date(month, year)
                self.__expiration_date = month + "/" + year
            else:
                self.__expiration_date = self.__generate_expiration_date()

            custom_card_issuer = input("Set the card issuer? (y/n): ")
            if custom_card_issuer.lower() == "y":
                self.__card_issuer = input("Enter card issuer: ")

            custom_cardholder_name = input("Specify the cardholder's name? (y/n): ")
            if custom_cardholder_name.lower() == "y":
                self.__cardholder_name = input("Enter cardholder's name: ")

            formatted_cc_number = ' '.join([self.__credit_card_number[i:i+4] for i in range(0, len(self.__credit_card_number), 4)])

            print("\nCredit Card Number: " + formatted_cc_number)
            print("Expiration Date: " + self.__expiration_date)
            print("CVV: " + self.__cvv)
            print("Card Issuer: " + self.__card_issuer)
            if self.__cardholder_name:
                print("Cardholder's Name: " + self.__cardholder_name)

        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

    def run(self):
        self.__run()


if __name__ == "__main__":
    cc_gen = CreditCardGenerator()
    cc_gen.run()
