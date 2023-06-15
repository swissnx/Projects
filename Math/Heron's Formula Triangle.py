
import math


class Triangle:
    def __init__(self):
        self.__a = None
        self.__b = None
        self.__c = None

    def __is_a_triangle(self):
        return (self.__a + self.__b > self.__c) and (self.__b + self.__c > self.__a) and (self.__c + self.__a > self.__b)

    def __herons_formula(self):
        s = (self.__a + self.__b + self.__c) / 2
        return math.sqrt(s * (s - self.__a) * (s - self.__b) * (s - self.__c))

    def __run(self):
        try:
            self.__a = float(input("Length of side a: "))
            self.__b = float(input("Length of side b: "))
            self.__c = float(input("Length of side c: "))
            if self.__is_a_triangle():
                area = self.__herons_formula()
                print(f"The area of the triangle is {area:.2f}. It is a triangle")
            else:
                print("Not a triangle!")
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

    def run(self):
        return self.__run()


if __name__ == "__main__":
    t = Triangle()
    t.run()
