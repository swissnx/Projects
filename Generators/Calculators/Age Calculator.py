
from datetime import datetime as dt, date


class AgeCalculator:
    def __init__(self):
        self.__today = dt.now().date()

    def __age_calculator(self, year: int, month: int, day: int) -> int:
        try:
            dob = date(year, month, day)
            age = int((self.__today - dob).days / 365.25)  # leap year is every 4 years (4 * 365 + 1 = 1461 days), 1461 / 4 = 365.25
            return age
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

    def __run(self):
        try:
            year = int(input("Year (YYYY): "))
            month = int(input("Month  (MM): "))
            day = int(input("Day    (DD): "))
            age = self.__age_calculator(year, month, day)
            print(f"\nAge is: {age}")

        except ValueError as ve:
            print(f"\n\u001b[3m** ValueError: \u001b[38;5;200m{ve}\u001b[0m")

        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

    def run(self):
        return self.__run()


if __name__ == "__main__":
    calculator = AgeCalculator()
    calculator.run()
