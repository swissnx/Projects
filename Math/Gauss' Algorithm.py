
class GaussSum:
    def __init__(self):
        self.__n = None

    def __run(self):
        try:
            self.__n = int(input("Number: "))
            sum = (self.__n * (self.__n + 1)) // 2
            print(f"The sum of the first {self.__n} natural numbers is: {sum}")
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;196m{e}\u001b[0m")

    def run(self):
        return self.__run()


if __name__ == "__main__":
    gauss_sum = GaussSum()
    gauss_sum.run()



# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ DOCUMENTATION ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #
# Note that Gauss’ algorithm is a simple formula to find the sum of the first n natural numbers. The formula is n(n+1)/2.
# When you entered 5 as the input for the GaussSum program, the output was 15 because the program calculates the sum of the first n natural numbers
# using Gauss’ formula: n(n+1)/2, where n is the input number. In this case, n is 5, so the formula becomes 5(5+1)/2, which equals 5*6/2, which equals 15.
# That’s why the output was 15. In other words, the program calculated the sum of the first 5 natural numbers: 1 + 2 + 3 + 4 + 5 = 15.
# Time complexity: O(1)
# Space complexity: O(1)