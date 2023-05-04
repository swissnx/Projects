class findBMI:
  def __init__(self, height, weight):
    self.__height = height / 100   # converting cm to m
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
