
from heapq import heappush, heappop


class MedianFinder:
    def __init__(self):
        self.__min_heap = []
        self.__max_heap = []

    def __add_num(self, num):
        if not self.__max_heap or num < -self.__max_heap[0]:
            heappush(self.__max_heap, -num)
        else:
            heappush(self.__min_heap, num)

        if len(self.__max_heap) > len(self.__min_heap) + 1:
            heappush(self.__min_heap, -heappop(self.__max_heap))
        elif len(self.__min_heap) > len(self.__max_heap):
            heappush(self.__max_heap, -heappop(self.__min_heap))

    def add_num(self, num):
        return self.__add_num(num)

    def __find_median(self):
        if len(self.__max_heap) == len(self.__min_heap):
            return (-self.__max_heap[0] + self.__min_heap[0]) / 2
        else:
            return -self.__max_heap[0]

    def find_median(self):
        return self.__find_median()

    def run(self):
        try:
            n = int(input("Number of values: "))

            for i in range(n):
                value = int(input(f"Enter value {i+1}: "))
                self.add_num(value)
            print("Median: ", self.find_median())

        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")


if __name__ == "__main__":
    median_finder = MedianFinder()
    median_finder.run()



# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ DOCUMENTATION ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #
# The MedianFinder class is used to find the median value of a set of numbers. The median is the middle value when a set of numbers
# is arranged in ascending order. If the set has an odd number of elements, the median is the middle element.
# If the set has an even number of elements, the median is the average of the two middle elements.