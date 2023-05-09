
# Liter/100km to Miles/Gallon & Miles/Gallon to Liter/100km

# converting l/100km into mpg, and vice versa.
# 1 American mile = 1609.344 metres
# 1 American gallon = 3.785411784 litres

def liters_100km_to_miles_gallon(litres):
    gallons = litres / 3.785411784
    miles = 100 * 1000 / 1609.344
    return miles / gallons

def miles_gallon_to_liters_100km(miles):
    km100 = miles * 1609.344 / 1000 / 100
    litres = 3.785411784
    return litres / km100


l_100km_mpg = liters_100km_to_miles_gallon(float(input("Enter liters here: ")))
mpg_l_100km = miles_gallon_to_liters_100km(float(input("Enter mpg here: ")))

print(l_100km_mpg)
print(mpg_l_100km)

# examples for l_100km_mpg: 3.9, 7.5, 10., 12
# examples for mpg: 60.3, 31.4, 23.5
