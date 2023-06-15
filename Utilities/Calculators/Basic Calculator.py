
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
