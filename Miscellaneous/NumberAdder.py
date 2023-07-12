
class NumberAdder:
    def __init__(self):
        self.__strings = input("Enter Numbers (separated with spaces): ").split()
        self.__total = 0

    def __add_numbers(self):
        for substr in self.__strings:
            try:
                self.__total += float(substr)

            except ValueError as ve:
                return f"\n\033[3m!✶ Error: \033[38;5;200m{ve}\033[0m"

    def result(self):
        try:
            self.__add_numbers()
            print(f"The total is: {self.__total}")
        
        except Exception as e:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")


if __name__ == "__main__":
    number_adder = NumberAdder()
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
