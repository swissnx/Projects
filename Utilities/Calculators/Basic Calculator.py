
import os


class Calculator:
    def __init__(self):
        self.__numbers = []
        self.__operators = []
        self.__result = 0

    def __calculate(self):
        self.__result = self.__numbers[0]

        for i, operator in enumerate(self.__operators):
            if operator == '+':
                self.__result += self.__numbers[i + 1]
            elif operator == '-':
                self.__result -= self.__numbers[i + 1]
            elif operator == '*':
                self.__result *= self.__numbers[i + 1]
            elif operator == '/':
                self.__result /= self.__numbers[i + 1]
            elif operator == '//':
                self.__result //= self.__numbers[i + 1]
            elif operator == '%':
                self.__result %= self.__numbers[i + 1]

    def __run(self):
        try:
            i = 0
            print(f"Result = {self.__result}")

            while True:
                num = input(f"\nNumber {i+1}: ")
                if num == "":
                    break
                else:
                    self.__numbers.append(float(num))
                    if i > 0:
                        if len(self.__numbers) > 1:
                            self.__calculate()
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(f"Result = {self.__result}")
                        print()

                    op = input("Operator: ")
                    if op == "":
                        break
                    else:
                        self.__operators.append(op)
                        i += 1

            print(f"\t = {self.__result}")

        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

    def run(self):
        return self.__run()


if __name__ == "__main__":
    c = Calculator()
    c.run()



# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ VERY BASIC FIRST CALCULATOR ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #

# not the answer we're looking for
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = num1 + num2
print(result)

# first_version of the correct calculator only w/ integers
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = int(num1) + int(num2)
print(result)

# second_version is the most optimal and correct w/ decimals
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)
print(result)



# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ BETTER CALCULATOR THAN ABOVE ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #

num1 = float(input("Enter first number: ")) #adding "float" to the input will convert "a potential string to an actual number
op = input("Enter operator: ") #here it'll be either addition/subtraction/multiplication or division.
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
elif op == "//":
    print(num1 // num2)
elif op == "%":
    print(num1 % num2)
else:
    print("Invalid operator")



# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ USING *ARGS ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #

def simple_numbers(*digits):
    sum = digits
    return sum

result = simple_numbers(14 + 56 + 10)
print("Sum = " + str(result))


def add_numbers(*args):
    return sum(args)

nums = []
while True:
    num = input("> ")
    if num == "stop":
        break
    nums.append(float(num))

result = add_numbers(*nums)
print("Sum = ", result)
