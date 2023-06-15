
class NumberAdder:
    def __init__(self, line: str):
        self.__strings = line.split()
        self.__total = 0

    def __add_numbers(self):
        for substr in self.__strings:
            try:
                self.__total += float(substr)
            except ValueError:
                print(substr, "is not a number.")

    def result(self):
        self.__add_numbers()
        print("The total is:", self.__total)


line = input("Enter Numbers (separated with spaces): ")
number_adder = NumberAdder(line)
number_adder.result()
