
CONVERSION_FACTORS = {
    'joule': {                                            # J
        'kilowatt-hour': 2.7777777777777777777777778E-7,  # kWh
        'calorie (th)': 0.23900573613766730401529637      # (th = thermochemical)
    },
    'kw/h': {
        'joule': 3600000,
        'calorie (th)': 860420.65009560229445506692
    },
    'calorie (th)': {
        'joule': 4.184,
        'kilowatt-hour': 1.1622222222222222222222222E-6
    }
}

# Define the conversion function
def convert_energy(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    else:
        factor = CONVERSION_FACTORS[from_unit][to_unit]
        return value * factor


# Test the function
print("\nChoose from:")
for i in CONVERSION_FACTORS.keys():
    print(i, end=", ")

from_unit = input("\n\n> ")
to_unit = input("> ")

value = float(input("\n> "))

result = convert_energy(value, from_unit, to_unit)
print(f'{value} {from_unit} = {result} {to_unit}')
