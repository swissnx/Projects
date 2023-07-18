
class HammingWeight:
    def __init__(self):
        self.__number = None

    def __hamming_weight(self):
        return bin(self.__number).count('1')

    def __run(self):
        try:
            self.__number = int(input("Number: "))
            result = self.__hamming_weight()
            print(f"The Hamming weight: {result}")
        except Exception as e:
            print(f"\n\u001b[3m** Error: \u001b[38;5;200m{e}\u001b[0m")

    def run(self):
        return self.__run()


if __name__ == "__main__":
    hw = HammingWeight()
    hw.run()



# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ DOCUMENTATION ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #
# This program calculates the Hamming weight of a given number. The Hamming weight is the number of 1s in the binary representation of the number.
# The program defines a class HammingWeight with a private attribute __number and three private methods: __hamming_weight, __run, and run.
# The __hamming_weight method calculates the Hamming weight of the number stored in the __number attribute.
# The __run method prompts the user to enter a number, stores it in the __number attribute, calls the __hamming_weight method to calculate the
# Hamming weight of this number, and prints the result. The run method is a public method that simply calls the private __run method.
# The main block of the program creates an instance of the HammingWeight class and calls its run method.
