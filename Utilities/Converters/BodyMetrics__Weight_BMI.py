
import time


class BodyMetrics:
    def __init__(self):
        self.__height = 0
        self.__weight = 0

    @staticmethod
    def __weight_converter():
        while True:
            try:
                weight = input("Weight: ")
                if not weight:
                    break
                weight = int(weight)
                unit = input("Lbs or Kg: ")
                if not unit:
                    break
            except ValueError as ve:
                print(f"Wrong input: {ve}")
                continue

            if unit.upper() in ["L", "LBS"]:
                converted = weight * 0.45
                print(f"Result: {converted} kgs")
            elif unit.upper() in ["K", "KG"]:
                converted = weight / 0.45
                print(f"Result: {converted} pounds")
            else:
                print("Please enter either 'k' or 'l' into a unit input")
                continue

            time.sleep(1)
            print("\n")

    @staticmethod
    def __ft_and_inch_to_m(ft, inch=0.0):
        return (ft * 0.3048) + (inch * 0.0254)

    @staticmethod
    def __lb_to_kg(lb):
        return lb * 0.45359237

    def __bmi(self):
        if self.__height < 1.0 or self.__height > 2.5 or self.__weight < 20 or self.__weight > 200:
            return None
        return self.__weight / (self.__height ** 2)

    def set_weight(self, weight, unit='kg'):
        if unit.lower() == 'lb':
            self.__weight = BodyMetrics.__lb_to_kg(weight)
        else:
            self.__weight = weight

    def set_height(self, height, unit='m'):
        if unit.lower() == 'ft':
            ft, inch = map(float, height.split())
            self.__height = BodyMetrics.__ft_and_inch_to_m(ft, inch)
        elif unit.lower() == 'cm':
            self.__height = height / 100
        else:
            self.__height = height

    def get_bmi(self):
        bmi = self.__bmi()
        result = []
        if bmi is not None:
            result.append(f"\nYour Body Mass Index is: {bmi:.2f}")
            if bmi <= 16:
                result.append("\nYou are severely underweight")
            elif bmi <= 18.5:
                result.append("\nYou are underweight")
            elif bmi <= 25:
                result.append("\nYou are healthy!")
            elif bmi <= 30:
                result.append("\nYou are overweight")
            else:
                result.append("\nYou are severely overweight")
        else:
            result.append("Invalid input for height or weight")
        return result

    def __run(self):
        print("\nOptions:\n1. Calculate BMI\n2. Convert Weight units?")
        choice = input("\nChoice: ")
        if choice.lower() == 'bmi' or choice == "1":
            height = input("Height #: ")
            height_unit = input("\nHeight unit (m/cm/ft): ")
            self.set_height(float(height), height_unit)

            weight = input("Weight #: ")
            weight_unit = input("Weight unit (kg/lb): ")
            self.set_weight(float(weight), weight_unit)

            results = self.get_bmi()
            for r in results:
                print(r)
        elif choice.lower() == 'weight' or choice == "2":
            print("Convert weight to KG or Lbs\n")
            BodyMetrics.__weight_converter()

    def run(self):
        return self.__run()


if __name__ == "__main__":
    body_metrics = BodyMetrics()
    body_metrics.run()




# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ DOCUMENTATION ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #
# BMI (body mass index) = weight in kilograms / height in meters**2
def bmi(weight, height):
    return weight / height ** 2
print(bmi(52.5, 1.65))
# but this one seem very simple and may give erroneous answers when complex numbers are entered.

# ====================================================================================================================================

def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
            weight < 20 or weight > 200:
        return None
    return weight / height ** 2
print(bmi(352.5, 1.65))
# Second, take a look at the way the backslash (\) symbol is used. If you use it in Python code and
# end a line with it, it will tell Python to continue the line of code in the next line of code.

#●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●

def lb_to_kg(lb):
    return lb * 0.45359237
print(lb_to_kg(1))

# And now it's time for feet and inches: 1 ft = 0.3048 m, and 1 in = 2.54 cm = 0.0254 m.
def ft_and_inch_to_m(ft, inch):
    return ft * 0.3048 + inch * 0.0254
print(ft_and_inch_to_m(1, 1))

# Sometimes you may want to use just feet without inches. Here the inch parameter has its default value equal to 0.0.
def ft_and_inch_to_m(ft, inch=0.0):
    return ft * 0.3048 + inch * 0.0254
print(ft_and_inch_to_m(6))

#●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●

# COMPLETE PROGRAM: what is the BMI of a person 5'7" tall and weighing 176 lbs?
def ft_and_inch_to_m(ft, inch=0.0):
    return (ft * 0.3048) + (inch * 0.0254)  # (1 ft * in m) + (1 in * in m)

def lb_to_kg(lb):
    return lb * 0.45359237  # (1 lb * in m)

def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
    return weight / (height ** 2)


person_weight = float(input("Weight: "))
person_height_ft = float(input("Height in ft: "))
person_height_in = float(input("Height in in: "))

show_bmi = bmi(weight=lb_to_kg(person_weight), height=ft_and_inch_to_m(person_height_ft, person_height_in))

print(f"{show_bmi:.2f}")
print("\n---------------------------\n")

def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
    return weight / (height ** 2)

person_weight = float(input("Weight in kg: "))
person_height_m = float(input("Height in m: "))

show_bmi = bmi(weight=person_weight, height=person_height_m)

print(f"{show_bmi:.2f}")

#●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●

# ✶✶✶✶✶✶✶✶✶ BMI (Body Mass Index) Calculator
class findBMI:
    def __init__(self, height, weight):
        self.__height = height / 100  # converting cm to m
        self.__weight = weight

    def convertions(self):
        BMI = self.__weight / (self.__height * self.__height)
        print(f"\nYour Body Mass Index is: {BMI:.2f}")
        return BMI


Height = float(input("Enter height in cm: "))
Weight = float(input("Enter weight in kg: "))

bmi_calculator = findBMI(Height, Weight)
BMI = bmi_calculator.convertions()

try:
    if BMI <= 16:
        print("\nYou are severely underweight")
    elif BMI <= 18.5:
        print("\nYou are underweight")
    elif BMI <= 25:
        print("\nYou are healthy!")
    elif BMI <= 30:
        print("\nYou are overweight")
    else:
        print("\nYou are severely overweight")

except TypeError as te:
    print(f"TypeError: {te}")

except Exception as e:
    print(f"There is a problem: {e}")

#●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●

# ✶✶✶✶✶✶✶✶✶ Weight Converter (Kg, Lbs)
#import time
class WeightConverter:
    def __init__(self):
        pass

    @staticmethod
    def __weight_converter():
        while True:
            try:
                weight = input("Weight: ")
                if not weight:
                    break
                weight = int(weight)
                unit = input("Lbs or Kg: ")
                if not unit:
                    break
            except ValueError as ve:
                print(f"Wrong input: {ve}")
                continue

            if unit.upper() in ["L", "LBS"]:
                converted = weight * 0.45
                print(f"Result: {converted} kgs")
            elif unit.upper() in ["K", "KG"]:
                converted = weight / 0.45
                print(f"Result: {converted} pounds")
            else:
                print("Please enter either 'k' or 'l' into a unit input")
                continue

            time.sleep(1)
            print("\n")

    @staticmethod
    def __run():
        print("Convert weight to KG or Lbs\n")
        WeightConverter.__weight_converter()

    @staticmethod
    def run():
        return WeightConverter.__run()


if __name__ == "__main__":
    weight_converter = WeightConverter()
    weight_converter.run()
