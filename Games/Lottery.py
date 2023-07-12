
class Lottery:
    def __init__(self):
        self.__numbers = []
        self.__user_numbers = []
    
    def __get_user_numbers(self):
        self.__user_numbers = []
        for i in range(6):
            number = int(input(f"Enter number {i+1}: "))
            self.__user_numbers.append(number)
    
    def __generate_numbers(self):
        from random import randint
        self.__numbers = []
        for i in range(6):
            number = randint(1, 100)
            while number in self.__numbers:
                number = randint(1, 100)
            self.__numbers.append(number)
    
    def __compare_numbers(self):
        matches = 0
        for number in self.__user_numbers:
            if number in self.__numbers:
                matches += 1
        return matches
    
    def __run(self):
        print("Welcome to the Lottery Game!")

        self.__get_user_numbers()
        self.__generate_numbers()
        matches = self.__compare_numbers()

        print(f"\nYour numbers: {self.__user_numbers}")
        print(f"Lottery numbers: {self.__numbers}")
        print(f"\nYou matched {matches} numbers!")

    def run(self):
        try:
            self.__run()

        except Exception as e:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")


if __name__ == "__main__":
    lottery = Lottery()
    lottery.run()
