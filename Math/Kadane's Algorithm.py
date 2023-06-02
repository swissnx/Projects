
class Kadane:
    def __init__(self):
        self.__array = None
        self.__max_sum = None

    def __kadane_algorithm(self):
        max_ending_here = max_so_far = self.__array[0]
        for element in self.__array[1:]:
            max_ending_here = max(element, max_ending_here + element)
            max_so_far = max(max_so_far, max_ending_here)
        self.__max_sum = max_so_far

    def __run(self):
        try:
            n = int(input("Number of elements: "))
            self.__array = list(map(int, input("Enter the elements (','): ").split(",")))
            if len(self.__array) != n:
                raise Exception("Invalid number of elements")
            self.__kadane_algorithm()
            print(f"Maximum subarray sum: {self.__max_sum}")
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

    def run(self):
        return self.__run()


if __name__ == "__main__":
    k = Kadane()
    k.run()



# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ DOCUMENTATION ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #
# Kadane’s algorithm is a way to find the largest sum of a continuous group of numbers within a larger group of numbers.
# Imagine you have a list of numbers, some positive and some negative. Kadane’s algorithm can help you find the group of numbers
# within that list that, when added together, give the largest sum.

# This can be useful in many situations. For example, imagine you are an investor looking at the daily changes in the value of a stock.
# You want to find the best time to buy and sell the stock to maximize your profit. You can use Kadane’s algorithm to find
# the period of time during which the stock had the largest overall increase in value.