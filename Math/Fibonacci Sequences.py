
class Fibonacci:
    def __init__(self):
        self.__start = None
        self.__end = None

    def __fibonacci(self, num):
        if num < 1:
            return None
        if num < 3:
            return 1

        elem1 = elem2 = 1
        total = 0
        for i in range(3, num + 1):
            total = elem1 + elem2
            elem1, elem2 = elem2, total
        return total

    def __run(self):
        try:
            self.__start = int(input("Starting point: "))
            self.__end = int(input("Ending point: "))
            print()
            for num in range(self.__start, self.__end):
                print(f"{num} - {self.__fibonacci(num)}")
            print()
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

    def run(self):
        return self.__run()


if __name__ == "__main__":
    fib = Fibonacci()
    fib.run()
