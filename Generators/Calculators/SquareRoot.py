
import math


class SquareRoot:
    def __init__(self):
        pass

    @staticmethod
    def __calculate_square_root(num: float) -> float:
        sqroot = math.sqrt(num)
        return sqroot

    @staticmethod
    def __run():
        while True:
            try:
                num = input("√x num: ")
                if not num:
                    break
                num = float(num)
                sqroot = SquareRoot.__calculate_square_root(num)
                print(f"= {sqroot:.2f}\n")

            except ValueError as ve:
                print(f"\n\u001b[3m** ValueError: \u001b[38;5;200m{ve}\u001b[0m")
            except Exception as e:
                print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

    @staticmethod
    def run():
        return SquareRoot.__run()


if __name__ == "__main__":
    calculator = SquareRoot()
    calculator.run()



# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ DOCUMENTATION ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #
#import math
def squareroot():
    while True:
        num = input("√sq number: ")
        if not num:
            break
        num = float(num)
        sqroot = math.sqrt(num)
        print(f"= {sqroot:.2f}\n")

squareroot()
