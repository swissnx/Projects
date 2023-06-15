
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
