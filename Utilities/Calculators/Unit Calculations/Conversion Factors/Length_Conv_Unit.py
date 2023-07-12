
CONVERSION_FACTORS = {
    'millimeter': {           # mm
        'centimeter': 0.1,    # cm
        'meter': 0.001,       # m
        'kilometer': 1.0e-6,  # km
        'inch': 0.0393700787401574803149606299213,   # in
        'feet': 0.00328083989501312335958005249344,  # ft
        'yard': 0.00109361329833770778652668416448,  # yd
        'mile': 6.21371192237333969617434184363E-7   # mi
    },
    'centimeter': {
        'millimeter': 10,
        'meter': 0.01,
        'kilometer': 1.0e-5,
        'inch': 0.393700787401574803149606299213,
        'feet': 0.0328083989501312335958005249344,
        'yard': 0.0109361329833770778652668416448,
        'mile': 6.21371192237333969617434184363E-6
    },
    'meter': {
        'millimeter': 1000,
        'centimeter': 100,
        'kilometer': 0.001,
        'inch': 39.3700787401574803149606299213,
        'feet': 3.28083989501312335958005249344,
        'yard': 1.09361329833770778652668416448,
        'mile': 6.21371192237333969617434184363E-4
    },
    'kilometer': {
        'millimeter': 1.0e+6,
        'centimeter': 1.0e+5,
        'meter': 1000,
        'inch': 39370.0787401574803149606299213,
        'feet': 3280.83989501312335958005249344,
        'yard': 1093.61329833770778652668416448,
        'mile': 0.621371192237333969617434184363
    },
    'inch': {
        'millimeter': 25.4,
        'centimeter': 2.54,
        'meter': 0.0254,
        'kilometer': 2.54e-5,
        'feet': 0.0833333333333333333333333333333,
        'yard': 0.0277777777777777777777777777778,
        'mile': 1.57828282828282828282828282828E-5
    },
    'feet': {
        'millimeter': 304.8,
        'centimeter': 30.48,
        'meter': 0.3048,
        'kilometer': 3.048E-4,
        'inch': 12,
        'yard': 0.333333333333333333333333333333,
        'mile': 1.89393939393939393939393939394E-4
    },
    'yard': {
        'millimeter': 914.4,
        'centimeter': 91.44,
        'meter': 0.9144,
        'kilometer': 9.144E-4,
        'inch': 36,
        'feet': 3,
        'mile': 5.68181818181818181818181818182E-4
    },
    'mile': {
        'millimeter': 1609344,
        'centimeter': 160934.4,
        'meter': 1609.344,
        'kilometer': 1.609344,
        'inch': 63360,
        'feet': 5280,
        'yard': 1760
    }
}


# Define the conversion function
def convert_length(value, from_unit, to_unit):
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

result = convert_length(value, from_unit, to_unit)
print(f'{value} {from_unit} = {result} {to_unit}')
