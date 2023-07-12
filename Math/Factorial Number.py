
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
            self.__start = int(input("Start-point: "))
            self.__end = int(input("End-point: "))

            print()
            for num in range(self.__start, self.__end):
                print(f"{num} - {self.__factorial(num)}")
            print()

        except Exception as e:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")

    def run(self):
        return self.__run()


if __name__ == "__main__":
    factorial = Factorial()
    factorial.run()



# ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●● FUNCTION ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●● #

import sys

sys.set_int_max_str_digits(0)

def factorial(num):
  if num <= 0:
    return None
  if num < 2:
    return 1

  fact = 1
  for i in range(2, num + 1):
    fact *= i
  return fact


start = int(input("Starting point: "))
end = int(input("Ending point:   "))
print()

for num in range(start, end):
  print(f"{num} - {factorial(num)}")



# ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●● DOCUMENTATION ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●● #

# 0! = 1 (yes! it's true)
# 1! = 1
# 2! = 1 * 2
# 3! = 1 * 2 * 3
# 4! = 1 * 2 * 3 * 4
# :
# :
# n! = 1 * 2 * 3 * 4 * ... * n-1 * n       # formula for the factorial of a non-negative integer n, n!. It represents the product of all positive integers up to and including n.
# n! = n * (n-1) * (n-2) * ... * 3 * 2 * 1
# It's marked with an exclamation mark, and is equal to the product of all natural numbers from one up to its argument.


def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product

for n in range(1, 6):  # testing
    print(f"{n} - {factorial_function(n)}")
# Notice how we mirror step by step the mathematical definition, and how we use the for loop to find the product.



# ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●● Comparing with: Recursion ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●● #

# The factorial has a second, recursive side too. Look:    n! = 1 × 2 × 3 × ... × n-1 × n
# It's obvious that:            1 × 2 × 3 × ... × n-1 = (n-1)!
# So, finally, the result is:   n! = (n-1)! × n

def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1)     # this is called recursion, because in return statement we are calling the function itself

abc = factorial_function(4)     # 4 * 3 * 2 * 1 = 24
print(abc)

# note: You also need to remember that recursive calls consume a lot of memory, and therefore may sometimes be inefficient.
