
class DigitOfLife:
    def __init__(self):
        self.__date = ""
        self.__the_sum = 0

    def __calculate_digit_of_life(self):
        if len(self.__date) != 8 or not self.__date.isdigit():
            raise ValueError("Invalid date format.")
        else:
            while len(self.__date) > 1:
                self.__the_sum = 0
                for dig in self.__date:
                    self.__the_sum += int(dig)
                self.__date = str(self.__the_sum)
            return self.__date

    def calculate_digit_of_life(self):
        return self.__calculate_digit_of_life()

    def __result(self):
        digit_of_life = self.__calculate_digit_of_life()
        return digit_of_life

    def result(self):
        return self.__result()

    def __run(self):
        while True:
            print("Enter your birthdate (in formats: YYYYMMDD or YYYYDDMM)")
            date = input("\nDate: ")

            try:
                self.__date = date
                print(f"Your Digit of Life is: {self.result()}")

            except ValueError as ve:
                return f"\n\033[3m!✶ Error: \033[38;5;200m{ve}\033[0m"

            except Exception as e:
                return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"
            
            repeat = input("\nTry again? (y/n): ")
            if repeat.lower() != 'y':
                break


if __name__ == "__main__":
    digit_of_life = DigitOfLife()
    digit_of_life.run()




# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ DOCUMENTATION ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #
""" Scenario
Some say that the Digit of Life is a digit evaluated using somebody's birthday. It's simple - you just need to sum all the digits of the date.
If the result contains more than one digit, you have to repeat the addition until you get exactly one digit. For example:

1 January 2017 = 2017 01 01
2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
1 + 2 = 3                                     3 is the digit we searched for and found.      """

date = input("Enter your birthdate (in the following format: YYYYMMDD or YYYYDDMM, 8 digits): ")
if len(date) != 8 or not date.isdigit():
    print("Invalid date format.")
else:
    while len(date) > 1:
        the_sum = 0
        for dig in date:
            the_sum += int(dig)
        print(date)
        date = str(the_sum)
    print(f"Your Digit of Life is: {date}")
