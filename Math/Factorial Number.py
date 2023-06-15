
import sys


sys.set_int_max_str_digits(0)

class Factorial:
    def __init__(self):
        self.__start = None
        self.__end = None

    def __factorial(self, num):
        if num <= 0:
            return None
        if num < 2:
            return 1

        fact = 1
        for i in range(2, num + 1):
            fact *= i
        return fact

    def __run(self):
        try:
            self.__start = int(input("Starting point: "))
            self.__end = int(input("Ending point: "))
            print()
            for num in range(self.__start, self.__end):
                print(f"{num} - {self.__factorial(num)}")
            print()
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

    def run(self):
        return self.__run()


if __name__ == "__main__":
    factorial = Factorial()
    factorial.run()
