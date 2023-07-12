
import math


class ShapeArea:
    def __init__(self):
        self.__pi = math.pi

    def __area_of_triangle(self, base, height):
        return 0.5 * base * height

    def area_of_triangle(self, base, height):
        return self.__area_of_triangle(base, height)

    def __area_of_square(self, side):
        return side ** 2

    def area_of_square(self, side):
        return self.__area_of_square(side)

    def __area_of_cylinder(self, radius, height):
        return 2 * self.__pi * radius * height + 2 * self.__pi * radius ** 2

    def area_of_cylinder(self, radius, height):
        return self.__area_of_cylinder(radius, height)

    def __area_of_sphere(self, radius):
        return 4 * self.__pi * radius ** 2

    def area_of_sphere(self, radius):
        return self.__area_of_sphere(radius)

    def __area_of_cube(self, side):
        return 6 * side ** 2

    def area_of_cube(self, side):
        return self.__area_of_cube(side)

    def __area_of_circle(self, radius):
        return self.__pi * radius ** 2

    def area_of_circle(self, radius):
        return self.__area_of_circle(radius)

    def __area_of_rectangle(self, length, width):
        return length * width

    def area_of_rectangle(self, length, width):
        return self.__area_of_rectangle(length, width)

    def run(self):
        try:
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            print(f"\nThe area of the triangle is {self.area_of_triangle(base, height)}")

            side = float(input("Enter the side of the square: "))
            print(f"\nThe area of the square is {self.area_of_square(side)}")

            radius = float(input("Enter the radius of the cylinder: "))
            height = float(input("Enter the height of the cylinder: "))
            print(f"\nThe area of the cylinder is {self.area_of_cylinder(radius, height)}")

            radius = float(input("Enter the radius of the sphere: "))
            print(f"\nThe area of the sphere is {self.area_of_sphere(radius)}")

            side = float(input("Enter the side of the cube: "))
            print(f"\nThe area of the cube is {self.area_of_cube(side)}")

            radius = float(input("Enter the radius of the circle: "))
            print(f"\nThe area of the circle is {self.area_of_circle(radius)}")

            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            print(f"\nThe area of the rectangle is {self.area_of_rectangle(length, width)}")

        except Exception as e:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")


if __name__ == "__main__":
    shape_area = ShapeArea()
    shape_area.run()





# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ DOCUMENTATION ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #
# example:
from area import ShapeArea   #if above code is saved in area.py file

sa = ShapeArea()
x = sa.area_of_triangle(5, 6)
print(x)