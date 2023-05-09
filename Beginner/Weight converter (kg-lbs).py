
import time

def func():
    while True:
        weight = int(input("Weight: "))
        unit = input("Lbs or Kg: ")

        if unit.upper() == "L":
            converted = weight * 0.45
            print(f"Result: {converted} kgs")
            time.sleep(3)
            print("\n")

        elif unit.upper() == "K":
            converted = weight / 0.45
            print(f"Result: {converted} pounds")
            time.sleep(3)
            print("\n")

        else:
            print("Please, enter either 'k' or 'l' into a unit input")
            time.sleep(3)
            print("\n")

    weight = int(input("Weight: "))
    unit = int(input("Lbs or Kg: "))

print("Convert weight to KG or Lbs:", "\n")
func()
