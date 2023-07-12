
class Euclid:
    def __init__(self):
        self.__a = None
        self.__b = None
        self.__gcd = None

    def __euclid_algorithm(self):
        while self.__b:
            self.__a, self.__b = self.__b, self.__a % self.__b
        self.__gcd = self.__a

    def __run(self):
        try:
            self.__a, self.__b = map(int, input("Enter two numbers: ").split())
            if self.__a < 1 or self.__b < 1:
                raise Exception("Invalid numbers")
            self.__euclid_algorithm()
            print(f"GCD: {self.__gcd}")

        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

    def run(self):
        return self.__run()


if __name__ == "__main__":
    e = Euclid()
    e.run()

# test cases: 10 5, 48 36



# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ DOCUMENTATION ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #
# This program calculates the greatest common divisor (GCD) of two numbers using Euclid’s algorithm. The GCD of two numbers is the largest positive integer that
# divides both numbers without a remainder. Euclid’s algorithm is an efficient way to calculate the GCD of two numbers by repeatedly applying the modulo operation.

# The program takes input from the user for the two numbers and then calculates their GCD using Euclid’s algorithm.
# The program is implemented as a class with private attributes and methods. The run method can be called to run the program and take input from the user.

# This program can be useful for calculating the GCD of two numbers for mathematical or educational purposes.
# It is designed to be reusable and can be easily integrated into other programs.