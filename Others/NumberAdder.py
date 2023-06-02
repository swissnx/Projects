
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



# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ DOCUMENTATION ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #

line = input("Enter a line of numbers - separate them with spaces: ")   # ask the user to enter a line filled with any number of numbers (the numbers can be floats)
strings = line.split()                                                  # split the line receiving a list of substrings;
total = 0                                                               # initiate the total sum to zero;
try:                            # as the string-float conversion may raise an exception, it's best to continue with the protection of the try-except block;
    for substr in strings:
        total += float(substr)       # ...and try to convert all its elements into float numbers; if it works, increase the sum;
    print("The total is:", total)
except:
    print(substr, "is not a number.")
