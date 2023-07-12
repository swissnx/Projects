
import random


class DiceRoller:
    def __init__(self):
        self.__sides = 6
        self.__dice = 1

    def __set_sides(self, sides):
        while True:
            try:
                self.__sides = int(sides)
                break

            except ValueError:
                print(f"\n\033[3m!✶ Error: \033[38;5;200mInvalid input. Please enter an integer.\033[0m")

    def __set_dice(self, dice):
        while True:
            try:
                self.__dice = int(dice)
                break

            except ValueError:
                print(f"\n\033[3m!✶ Error: \033[38;5;200mInvalid input. Please enter an integer.\033[0m")

    def __roll_dice(self):
        rolls = []
        for i in range(self.__dice):
            roll = random.randint(1, self.__sides)
            rolls.append(roll)
        return rolls

    def __run(self):
        try:
            sides = input("Sides: ")
            self.__set_sides(sides)

            dice = input("Number of Dice: ")
            self.__set_dice(dice)

            while True:
                rolls = self.__roll_dice()
                print(f"\nRolls: {rolls}")

                again = input("Try again? (y/n): ")
                if again.lower() != 'y':
                    break

        except Exception as e:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")

    def run(self):
        return self.__run()


if __name__ == "__main__":
    roller = DiceRoller()
    roller.run()
