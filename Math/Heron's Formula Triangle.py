
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



# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ DOCUMENTATION ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #
# ✶✶✶ Heron's formula ✶✶✶
#   s = (a + b + c) / 2
#   A = sqrt(s (s - a)(s - b)(s - c))          Note: sqrt(x) = x**0.5


# example of all above codes in action:
def heron(a, b, c):
  p = (a + b + c) / 2
  return (p * (p - a) * (p - b) * (p - c))**0.5

#●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●

def is_a_triangle(a, b, c):
  return a + b > c and b + c > a and c + a > b

def heron(a, b, c):
  p = (a + b + c) / 2
  return (p * (p - a) * (p - b) * (p - c))**0.5

def area_of_triangle(a, b, c):
  if not is_a_triangle(a, b, c):    # this line refers to the first function. If it will come out as True -> (not True = False), if False, it will print None.
    return None
  return heron(a, b, c)

print(area_of_triangle(1., 1., 2.**.5))

# It's very close to 0.5, but it isn't exactly 0.5. What does it mean? Is it an error?
# No, it isn't. This is the specifics of floating-point calculations. We'll tell you more about it soon.


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def is_a_triangle(a, b, c):
    return a+b > c and b+c > a and c+a > b

a = float(input("Enter the first side's length: "))
b = float(input("Enter the second side's length: "))
c = float(input("Enter the third side's length: "))

if is_a_triangle(a, b, c):
    print("\nYes, it can be a triangle.")
else:
    print("No, it can't be a triangle.")

# We will need to make use of the Pythagorean theorem: c2 = a2 + b2  .  The hypotenuse is the longest side.
def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c**2 == a**2 + b**2
    if a > b and a > c:
        return a**2 == b**2 + c**2


print("\n", is_a_right_triangle(5, 3, 4))  # Yes, it is a triangle
print(is_a_right_triangle(1, 3, 4))        # No, not a triangle

#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
# its step-by-step building/calculations:
def is_a_triangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True

#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
# This is a compact version:
def is_a_triangle(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True

print(is_a_triangle(1, 1, 1))  # True
print(is_a_triangle(1, 1, 3))  # False

#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
# This is a more compact version:
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

print(is_a_triangle(1, 1, 1))  # True
print(is_a_triangle(1, 1, 3))  # False

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
