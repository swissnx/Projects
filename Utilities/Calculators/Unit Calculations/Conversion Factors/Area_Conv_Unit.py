
CONVERSION_FACTORS = {
    'square millimeter': {           # mm2
        'square centimeter': 0.01,   # cm2
        'square meter': 1e-6,        # m2
        'hectare': 1e-8,             # ha
        'square kilometer': 1.E-12,  # km2
        'square inch': 0.00155000310000620001240002480005, # sq in
        'square foot': 1.07639104167097223083335055559E-5, # sq ft
        'square yard': 1.19599004630108025648150061732E-6, # sq yd
        'acre': 2.47105381467165342248243929199E-10        # ac
    },
    'square centimeter': {
        'square millimeter': 100,
        'square meter': 1.E-4,
        'hectare': 1.E-8,
        'square kilometer': 1.E-10,
        'square inch': 0.155000310000620001240002480005,
        'square foot': 0.00107639104167097223083335055559,
        'square yard': 1.19599004630108025648150061732E-4,
        'acre': 2.47105381467165342248243929199E-8
    },
    'square meter': {
        'square millimeter': 1e+6,
        'square centimeter': 10000,
        'hectare': 1.E-4,
        'square kilometer': 1.E-6,
        'square inch': 1550.00310000620001240002480005,
        'square foot': 10.7639104167097223083335055559,
        'square yard': 1.19599004630108025648150061732,
        'acre': 2.47105381467165342248243929199E-4
    },
    'hectare': {
        'square millimeter': 1e+10,
        'square centimeter': 1e+8,
        'square meter': 10000,
        'square kilometer': 0.01,
        'square inch': 15500031.0000620001240002480005,
        'square foot': 107639.104167097223083335055559,
        'square yard': 11959.9004630108025648150061732,
        'acre': 2.47105381467165342248243929199
    },
    'square kilometer': {
        'square millimeter': 1000000000000,
        'square centimeter': 10000000000,
        'square meter': 1000000,
        'hectare': 100,
        'square inch': 1550003100.00620001240002480005,
        'square foot': 10763910.4167097223083335055559,
        'square yard': 1195990.04630108025648150061732,
        'acre': 247.105381467165342248243929199
    },
    'square inch': {
        'square millimeter': 645.16,
        'square centimeter': 6.4516,
        'square meter': 6.4516E-4,
        'hectare': 6.4516e-8,
        'square kilometer': 6.4516E-10,
        'square foot': 0.00694444444444444444444444444444,
        'square yard': 7.71604938271604938271604938272E-4,
        'acre': 1.5942250790736E-7
    },
    'square foot': {
        'square millimeter': 92903.04,
        'square centimeter': 929.0304,
        'square meter': 0.09290304,
        'hectare': 9.290304E-6,
        'square kilometer': 9.290304E-8,
        'square inch': 144,
        'square yard': 0.111111111111111111111111111111,
        'acre': 2.29568411386593204775022956841E-5
    },
    'square yard': {
        'square millimeter': 836127.36,
        'square centimeter': 8361.2736,
        'square meter': 0.83612736,
        'hectare': 8.3612736E-5,
        'square kilometer': 8.3612736E-7,
        'square inch': 1296,
        'square foot': 9,
        'acre': 2.06611570247933884297520661157E-4
    },
    'acre': {
        'square millimeter': 4046856422.4,
        'square centimeter': 40468564.224,
        'square meter': 4046.8564224,
        'hectare': 0.40468564224,
        'square kilometer': 0.0040468564224,
        'square inch': 6272640,
        'square foot': 43560,
        'square yard': 4840
    }
}

# Define the conversion function
def convert_area(value, from_unit, to_unit):
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

result = convert_area(value, from_unit, to_unit)
print(f'{value} {from_unit} = {result} {to_unit}')
