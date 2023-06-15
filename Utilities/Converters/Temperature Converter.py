
class TemperatureConverter:
    def __init__(self):
        self.__temperature = 0
        self.__unit = 'Celsius'

    def __str__(self):
        return f"{self.__temperature:.2f} {self.__unit}"

    def __convert_to_celsius(self, temperature, unit):
        unit = unit.lower()
        if unit == 'fahrenheit' or unit == 'f':
            return (temperature - 32) * 5/9
        elif unit == 'kelvin' or unit == 'k':
            return temperature - 273.15
        else:
            return temperature

    def __convert_from_celsius(self, temperature, unit):
        unit = unit.lower()
        if unit == 'fahrenheit' or unit == 'f':
            return (temperature * 9/5) + 32
        elif unit == 'kelvin' or unit == 'k':
            return temperature + 273.15
        else:
            return temperature

    def set(self, temperature, unit):
        self.__temperature = self.__convert_to_celsius(temperature, unit)
        self.__unit = 'Celsius'

    def get(self, unit):
        return self.__convert_from_celsius(self.__temperature, unit)

    def __run(self):
        try:
            while True:
                temperature = float(input('\nEnter the temperature: '))
                unit = input('\nUnits:\n1. Celsius\n2. Fahrenheit\n3. Kelvin\n\n> ')
                self.set(temperature, unit)
                print(f"\nC: {self.get('Celsius'):.2f} °C")
                print(f"F: {self.get('Fahrenheit'):.2f} F")
                print(f"K: {self.get('Kelvin'):.2f} K")
                again = input("\nTry again? (y/n): ")
                if again.lower() == '' or again.lower() == 'n':
                    break
                elif again.lower() != 'y':
                    raise Exception("Invalid input")
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

    def run(self):
        self.__run()


if __name__ == "__main__":
    temp_conv = TemperatureConverter()
    temp_conv.run()
