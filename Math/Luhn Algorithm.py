
class Luhn:
    def __init__(self):
        self.__card_number = input("Enter a card number: ")

    def __luhn_algorithm(self):
        card_number = [int(digit) for digit in self.__card_number]
        check_digit = card_number.pop(-1)
        card_number.reverse()

        for index, digit in enumerate(card_number):
            if index % 2 == 0:
                doubled_digit = digit * 2
                if doubled_digit > 9:
                    doubled_digit -= 9
                card_number[index] = doubled_digit

        total = sum(card_number) + check_digit

        return total % 10 == 0

    def run(self):
        try:
            if self.__luhn_algorithm():
                print("Valid card number")
            else:
                print("Invalid card number")
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")


if __name__ == "__main__":
    luhn = Luhn()
    luhn.run()
