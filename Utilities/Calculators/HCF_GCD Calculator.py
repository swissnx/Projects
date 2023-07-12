
class HCF_GCD:
    def __init__(self):
        self.__num1 = int(input("Number #1: "))
        self.__num2 = int(input("Number #2: "))

    def __hcf(self):
        try:
            if self.__num1 > self.__num2:
                smaller = self.__num2

            else:
                smaller = self.__num1

            for i in range(1, smaller + 1):
                if (self.__num1 % i == 0) and (self.__num2 % i == 0):
                    hcf = i

            return hcf

        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def __gcd(self):
        return (self.__num1 * self.__num2) // self.__hcf()

    def __run(self):
        try:
            print(f"\nThe Highest Common Factor of {self.__num1} and {self.__num2} is: {self.__hcf()}")
            print(f"The Greatest Common Divisor of {self.__num1} and {self.__num2} is: {self.__gcd()}")

        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def run(self):
        return self.__run()


if __name__ == "__main__":
    hcf_gcd = HCF_GCD()
    hcf_gcd.run()



# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ DOCUMENTATION ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #
""" This code calculates the Highest Common Factor (HCF), also known as the Greatest Common Divisor (GCD), of two integers entered by the user.
The HCF is the largest positive integer that divides both numbers without a remainder.

First, the code prompts the user to enter two integers. Then it determines which of the two numbers is smaller and assigns it to the variable mx.
The code then uses a for loop to iterate through all the numbers from 1 to mx. For each iteration, it checks if both num1 and num2 are divisible
by the current value of i without a remainder. If they are, it assigns the value of i to the variable hcf. Finally, after the loop has completed,
it prints the value of hcf, which is the highest common factor of the two numbers entered by the user.


The Highest Common Factor (HCF), also known as the Greatest Common Divisor (GCD), is the largest positive integer that divides two or more integers
without a remainder. In other words, it is the largest number that is a factor of two or more numbers.

For example, the HCF/GCD of 12 and 18 is 6, because 6 is the largest number that divides both 12 and 18 without a remainder.

The HCF/GCD can be calculated using various methods, such as the Euclidean algorithm or prime factorization.
In the HCF_GCD class, the HCF is calculated by finding the largest common factor of the two numbers. """