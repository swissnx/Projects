
class PerfectNumber:
    def __init__(self):
        self.__number = None
        self.__is_perfect = None

    def __check_perfect(self):
        divisors = [1]
        for i in range(2, int(self.__number ** 0.5) + 1):
            if self.__number % i == 0:
                divisors.extend([i, self.__number // i])
        if sum(divisors) == self.__number:
            self.__is_perfect = True
        else:
            self.__is_perfect = False

    def __run(self):
        try:
            self.__number = int(input("Number: "))
            if self.__number < 1:
                raise Exception("Invalid number")
            self.__check_perfect()
            if self.__is_perfect:
                print(f"{self.__number} is a perfect number.")
            else:
                print(f"{self.__number} is NOT a perfect number.")
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

    def run(self):
        return self.__run()


if __name__ == "__main__":
    pn = PerfectNumber()
    pn.run()

# test cases: 6, 28, 496



# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ DOCUMENTATION ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #
# This program checks if a given number is a perfect number. A perfect number is a positive integer that is equal to the sum of its
# proper divisors (excluding itself). For example, 6 is a perfect number because its proper divisors are 1, 2, and 3, and 1 + 2 + 3 = 6.

# The program takes input from the user for the number to check and then checks if it is a perfect number. The program is implemented as a class
# with private attributes and methods. The run method can be called to run the program and take input from the user.

# This program can be useful for checking if a given number is a perfect number for mathematical or educational purposes.
# It is designed to be reusable and can be easily integrated into other programs.