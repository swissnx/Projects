
class IsAHappyNumber:
    def __init__(self):
        self.__number = input("Number: ")

    def __is_happy(self, n):
        seen = set()
        while n not in seen:
            seen.add(n)
            n = _sum(int(i) ** 2 for i in str(n))
        return n == 1

    def __run(self):
        while True:
            if self.__number == "":
                break
            self.__number = int(self.__number)
            if self.__is_happy(self.__number):
                print(f"\n{self.__number} is a happy number")
            else:
                print(f"\n{self.__number} is not a happy number")
            self.__number = input("\nNumber: ")
    
    def run(self):
        try:
            self.__run()
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")


if __name__ == "__main__":
    h_num = IsAHappyNumber()
    h_num.run()
