
class FuelEfficiency:
    def __init__(self):
        self.__liters_per_gallon = 3.785411784
        self.__miles_per_100km = 100 * 1000 / 1609.344

    def __liters_100km_to_mpg(self, liters):
        gallons = liters / self.__liters_per_gallon
        return self.__miles_per_100km / gallons

    def liters_100km_to_mpg(self, liters):
        return self.__liters_100km_to_mpg(liters)

    def __mpg_to_liters_100km(self, miles):
        km100 = miles * 1609.344 / 1000 / 100
        return self.__liters_per_gallon / km100

    def mpg_to_liters_100km(self, miles):
        return self.__mpg_to_liters_100km(miles)

    def __run(self):
        try:
            while True:
                try:
                    liters = float(input("Enter liters per 100km: "))
                    mpg = float(input("Enter miles per gallon: "))
                    break
                
                except ValueError as ve:
                    return f"\n\033[3m!✶ Error: \033[38;5;200m{ve}\033[0m"

            l_100km_mpg = self.__liters_100km_to_mpg(liters)
            mpg_l_100km = self.__mpg_to_liters_100km(mpg)

            print(f"{liters} liters/100km is equivalent to {l_100km_mpg:.2f} mpg")
            print(f"{mpg} mpg is equivalent to {mpg_l_100km:.2f} liters/100km")

        except ValueError as ve:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{ve}\033[0m"

        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def run(self):
        return self.__run()


if __name__ == "__main__":
    fuelconverter = FuelEfficiency()
    fuelconverter.run()



# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ DOCUMENTATION ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #
# Liter/100km to Miles/Gallon & Miles/Gallon to Liter/100km

# converting l/100km into mpg, and vice versa.
# 1 American mile = 1609.344 metres
# 1 American gallon = 3.785411784 litres

# examples for l_100km_mpg: 3.9, 7.5, 10., 12
# examples for mpg: 60.3, 31.4, 23.5