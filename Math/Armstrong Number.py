
class ArmstrongChecker:
    def __init__(self):
        self.__number = None

    def __is_armstrong(self):
        num_str = str(self.__number)
        num_digits = len(num_str)
        sum = 0
        for digit in num_str:
            sum += int(digit) ** num_digits
        return sum == self.__number

    def __run(self):
        try:
            self.__number = int(input("Check the Number: "))
            if self.__is_armstrong():
                print(f"{self.__number} is an Armstrong number.")
            else:
                print(f"{self.__number} is not an Armstrong number.")
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")
    
    def run(self):
        return self.__run()


if __name__ == "__main__":
    checker = ArmstrongChecker()
    checker.run()



# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ DOCUMENTATION ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #
# Note that an Armstrong number is a n-digit number that is equal to the sum of each of its digits raised to the nth power.
# Example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153   (153 has 3 digits, so each separated digit is raised to the power of 3)
# For example:  1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, and 1634 are all Armstrong numbers
# Time complexity: O(nlog2(n))
# Space complexity: O(1)
