
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
        self.__primes = []

        for i in range(1, self.__prime + 1):
            if self.__is_prime(i + 1):
                self.__primes.append(str(i + 1))

        return ", ".join(self.__primes) + "."

    def run(self):
        try:
            print("\nFind a Prime Number.")
            self.__prime = int(input("\nList numbers until: "))
            print(self.__prime_num())

            print("\nOne more list?\n")
            while True:
                answer = input("Enter (y/n): ")
                if answer.lower() == "y":
                    self.run()
                    break
                elif answer.lower() == "n" or answer == "":
                    break
                else:
                    print("\nWrong Input. Try again.\n")

        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;196m{e}\u001b[0m")


if __name__ == "__main__":
    pn = PrimeNumber()
    pn.run()



# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ FUNCTION ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #

def is_prime(num):
    for i in range(2, int(1 + num ** 0.5)):
        if num % i == 0:
            return False
    return True

def prime_num():
    prime = input("\nList numbers until: ")
    if not prime:
        return
    prime = int(prime)
    primes = []
    for i in range(1, prime + 1):
        if is_prime(i + 1):
            primes.append(str(i + 1))
    print(", ".join(primes) + ".")
    print("\nOne more list?\n")
    answer = input("Enter (y/n): ")
    while True:
        if answer.lower() == "y":
            prime_num()
            break
        elif answer.lower() == "n" or answer == "":
            break
        else:
            print("\nWrong Input. Try again.\n")
            answer = input("Enter (y/n): ")

print("\nFind a Prime Number.")
prime_num()



# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ DOCUMENTATION ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #
# the statement "num ** 0.5" calculates the square root of the number 'num'.
# For example, let's say 'num' is 16. The statement "num ** 0.5" would calculate the square root of 16, which is 4.
# So in short, the statement "num ** 0.5" calculates the square root of 'num' by raising 'num' to the power of 0.5.