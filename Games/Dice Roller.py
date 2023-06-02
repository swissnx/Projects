
import random


class DiceRoller:
    def __init__(self):
        self.__sides = 6
        self.__dice = 1

    def __set_sides(self):
        while True:
            sides = input("Sides: ")
            try:
                self.__sides = int(sides)
                break
            except ValueError:
                print("\n\u001b[3m** An error occurred: \u001b[38;5;200mInvalid input. Please enter an integer.\u001b[0m")
            again = input("Try again? (y/n): ")
            if again.lower() != 'y':
                break

    def __set_dice(self):
        while True:
            dice = input("Number of Dice: ")
            try:
                self.__dice = int(dice)
                break
            except ValueError:
                print("\n\u001b[3m** An error occurred: \u001b[38;5;200mInvalid input. Please enter an integer.\u001b[0m")
            again = input("Try again? (y/n): ")
            if again.lower() != 'y':
                break

    def __roll_dice(self):
        rolls = []
        for i in range(self.__dice):
            roll = random.randint(1, self.__sides)
            rolls.append(roll)
        return rolls

    def __run(self):
        self.__set_sides()
        self.__set_dice()
        while True:
            rolls = self.__roll_dice()
            print(f"\nRolls: {rolls}")
            again = input("Try again? (y/n): ")
            if again.lower() != 'y':
                break

    def run(self):
        return self.__run()


if __name__ == "__main__":
    roller = DiceRoller()
    roller.run()
