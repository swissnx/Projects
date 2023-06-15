
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
# The Collatz Conjecture is an unsolved mathematical problem. It states that for any positive integer n, if you take the following process:
# • if n is even, divide it by 2
# • if n is odd, multiply it by 3 and add 1
# then you will always reach 1. This script is a simulation of the conjecture for a given value of c0.
