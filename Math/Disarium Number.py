
class DisariumChecker:
    def __init__(self):
        self.__number = None

    def __is_disarium(self):
        num_str = str(self.__number)
        sum = 0
        for i, digit in enumerate(num_str):
            sum += int(digit) ** (i + 1)
        return sum == self.__number

    def __run(self):
        try:
            self.__number = int(input("Check the Number: "))
            if self.__is_disarium():
                print(f"{self.__number} is a Disarium number.")
            else:
                print(f"{self.__number} is not a Disarium number.")
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

    def run(self):
        return self.__run()


if __name__ == "__main__":
    checker = DisariumChecker()
    checker.run()



# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ DOCUMENTATION ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #
# A Disarium number is a number in which the sum of its digits powered with their respective positions (from left to right starting from 1) is equal to the number itself.
# Example, 135 is a Disarium number because 1^1 + 3^2 + 5^3 = 135   (135 has 3 digits, so each separated digit is raised to the power of the number of 135)
# For example: 89 and 135 are Disarium numbers
# Time complexity: O(n)
# Space complexity: O(1)
