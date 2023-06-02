
class BoyerMooreMajorityVote:
    def __init__(self):
        self.__sequence = None
        self.__majority_element = None

    def __find_majority_element(self):
        element = None
        counter = 0
        for x in self.__sequence:
            if counter == 0:
                element = x
                counter = 1
            elif element == x:
                counter += 1
            else:
                counter -= 1
        return element

    def __verify_majority_element(self):
        count = 0
        for x in self.__sequence:
            if x == self.__majority_element:
                count += 1
        if count > len(self.__sequence) // 2:
            return True
        else:
            return False

    def __run(self):
        try:
            print("Enter a sequence of numbers separated by spaces")
            self.__sequence = list(map(int, input("> ").split()))
            self.__majority_element = self.__find_majority_element()
            if self.__verify_majority_element():
                print(f"The majority element is {self.__majority_element}")
            else:
                print("There is no majority element")
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

    def run(self):
        return self.__run()


if __name__ == "__main__":
    bm = BoyerMooreMajorityVote()
    bm.run()



# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ DOCUMENTATION ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #
# In the context of the Boyer-Moore majority vote algorithm, a majority element is defined as an element that occurs repeatedly for more than
# half of the elements of the input sequence. In other words, if the length of the input sequence is n, then a majority element must occur more than n/2 times.
# In the example you provided, the input sequence has 5 elements: 1 1 2 3 1. The element 1 occurs 3 times, which is not more than half of the length
# of the sequence (5/2 = 2.5). Therefore, there is no majority element in this sequence according to the definition used by the Boyer-Moore majority vote algorithm.