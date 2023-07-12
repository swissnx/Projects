
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
                return f"\n\033[3m!✶ Error: \033[38;5;200m{ve}\033[0m"
            
            except Exception as e:
                return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

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
