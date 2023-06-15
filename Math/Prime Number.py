
class PrimeNumber:
    def __init__(self):
        self.__prime = None
        self.__primes = []

    def __is_prime(self, num):
        for i in range(2, int(1 + num ** 0.5)):
            if num % i == 0:
                return False
        return True

    def __prime_num(self):
        self.__prime = int(input("\nList numbers until: "))
        self.__primes = []
        for i in range(1, self.__prime + 1):
            if self.__is_prime(i + 1):
                self.__primes.append(str(i + 1))
        print(", ".join(self.__primes) + ".")
        print("\nOne more list?\n")
        answer = input("Enter (y/n): ")
        while True:
            if answer.lower() == "y":
                self.__prime_num()
                break
            elif answer.lower() == "n" or answer == "":
                break
            else:
                print("\nWrong Input. Try again.\n")
                answer = input("Enter (y/n): ")

    def __run(self):
        try:
            print("\nFind a Prime Number.")
            self.__prime_num()
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;196m{e}\u001b[0m")

    def run(self):
        return self.__run()


if __name__ == "__main__":
    pn = PrimeNumber()
    pn.run()
