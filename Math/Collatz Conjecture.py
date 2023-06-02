
class CollatzConjecture:
    def __init__(self):
        self.__c0 = None
        self.__steps = 0

    def __collatz_conjecture(self):
        while self.__c0 != 1:
            if self.__c0 % 2 != 0:
                cnew = self.__c0 * 3 + 1
            else:
                cnew = self.__c0 // 2
            print(f"-> {self.__c0}")
            self.__c0 = cnew
            self.__steps += 1

    def __run(self):
        try:
            self.__c0 = int(input("Enter c0: "))
            if self.__c0 > 1:
                self.__collatz_conjecture()
                print(f"\nSteps = {self.__steps}\n")
            else:
                print("Bad c0 value")
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

    def run(self):
        return self.__run()


if __name__ == "__main__":
    cc = CollatzConjecture()
    cc.run()



# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ DOCUMENTATION ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #
# This code is a Python script that calculates the number of steps required to reach 1 in a mathematical process called the Collatz Conjecture.
c0 = int(input("Enter c0: "))     # The script prompts the user to enter an integer value for "c0", and stores it in the variable "c0".

if c0 > 1:                        # Checks if the value of "c0" is greater than 1. If the value of "c0" is greater than 1, the script performs the following actions:
    steps = 0                     # Initializes a variable "steps" to 0, which will be used to store the number of steps required to reach 1.
    while c0 != 1:                # Uses a "while" loop to iterate through the Collatz Conjecture process. The loop continues to run until the value of "c0" becomes 1.
        if c0 % 2 != 0:           # Inside the while loop, there is an "if-else" statement that checks if the value of "c0" is odd or even.
            cnew = c0 * 3 + 1     # If the value of "c0" is odd, it calculates the next value "cnew" of the Collatz Conjecture process by the formula 3 * c0 + 1.
        else:
            cnew = c0 // 2        # If the value of "c0" is even, it calculates the next value "cnew" of the Collatz Conjecture process by the formula c0 // 2.
        print(c0)                 # Prints the current value of "c0" using the "print" function.
        c0 = cnew                 # Assigns the value of "cnew" to "c0" in order to use it in the next iteration of the loop.
        steps += 1                # Increments the value of "steps" by 1, using the line "steps += 1"
    print(f"\nSteps = {steps}\n")   # The loop continues to run til the value of "c0" becomes 1, at this point the script prints the number of steps taken to reach 1.
else:
    print("Bad c0 value")         # If the value of "c0" is not greater than 1, the script enters the "else" block.


# The Collatz Conjecture is an unsolved mathematical problem. It states that for any positive integer n, if you take the following process:
# • if n is even, divide it by 2
# • if n is odd, multiply it by 3 and add 1
# then you will always reach 1. This script is a simulation of the conjecture for a given value of c0.