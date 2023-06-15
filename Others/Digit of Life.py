
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
        return f"Your Digit of Life is: {digit_of_life}"

    def result(self):
        return self.__result()

    def __run(self):
        while True:
            print("Enter your birthdate (in the following format: YYYYMMDD or YYYYDDMM)")
            date = input("\nDate: ")
            try:
                self.__date = date
                print(self.result())
            except ValueError as e:
                print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")
            repeat = input("\nWould you like to try again? (y/n): ")
            if repeat.lower() != 'y':
                break

    def run(self):
      return self.__run()


if __name__ == "__main__":
    digit_of_life = DigitOfLife()
    digit_of_life.run()
