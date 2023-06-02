
class MissingNumbers:
    def __init__(self):
        self.__nums = None

    def __run(self):
        try:
            print("Enter the array of numbers separated by spaces")
            self.__nums = list(map(int, input(">> ").split()))
            n = max(self.__nums)
            expected_nums = set(range(n + 1))
            missing_numbers = expected_nums - set(self.__nums)
            print(f"The missing numbers are: {', '.join(map(str, missing_numbers)) + '.'}")
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

    def run(self):
        return self.__run()


if __name__ == "__main__":
    missing_numbers = MissingNumbers()
    missing_numbers.run()



# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ DOCUMENTATION ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #
# Note that this program uses Gauss’ formula to find the missing number in an array of n distinct numbers in the range [0, n]. The formula is n(n+1)/2.
# Time complexity: O(n)
# Space complexity: O(1)
# This program takes an input array of n distinct numbers in the range [0, n] from the user and then calculates the expected sum of the first n natural numbers
# using Gauss’ formula: n(n+1)/2. It then calculates the actual sum of the numbers in the array and subtracts it from the expected sum to find the missing number.