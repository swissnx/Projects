
# The formula to convert regular ounces to troy ounces is:
# Troy ounces = Regular ounces / 31.1035

# A "troy ounce" (symbol: ozt) is a unit of weight commonly used for measuring precious metals such as gold, silver, and platinum.
# It is equivalent to 31.1034768 grams and is divided into 20 "pennyweights" or 480 "grains".

CONVERSION_FACTORS = {
    'milligram': {           # mg
        'carat': 0.005,      # ct
        'gram': 0.001,       # g
        'kilogram': 1.0e-6,  # kg
        'tonne': 1.0e-9,     # t
        'ounce': 3.52739619495804129156758082152E-5,  # oz
        'pound': 2.20462262184877580722973801345E-6,  # lb
        'troy ounce': 3.2150751458333E-5              # ozt
    },
    'carat': {
        'milligram': 200,
        'gram': 0.2,
        'kilogram': 2.E-4,  # 0.0002
        'tonne': 2.0E-7,
        'ounce': 0.00705479238991608258313516164304,
        'pound': 4.4092452436975516144594760269E-4,
        'troy ounce': 0.0064301493137256
    },
    'gram': {
        'milligram': 1000,
        'carat': 5,
        'kilogram': 0.001,
        'tonne': 1.0e-6,
        'ounce': 0.0352739619495804129156758082152,
        'pound': 0.00220462262184877580722973801345,
        'troy ounce': 0.032150746568628
    },
    'kilogram': {
        'milligram': 1.0e+6,
        'carat': 5000,
        'gram': 1000,
        'tonne': 0.001,
        'ounce': 35.2739619495804129156758082152,
        'pound': 2.20462262184877580722973801345,
        'troy ounce': 32.150746568628
    },
    'tonne': {
        'milligram': 1.0e+9,
        'carat': 5.0e+6,
        'gram': 1.0e+6,
        'kilogram': 1000,
        'ounce': 35273.9619495804129156758082152,
        'pound': 2204.62262184877580722973801345,
        'troy ounce': 32150.7466
    },
    'ounce': {
        'milligram': 28349.523125,
        'carat': 141.747615625,
        'gram': 28.349523125,
        'kilogram': 0.028349523125,
        'tonne': 2.8349523125E-5,
        'pound': 0.0625,
        'troy ounce': 0.91145833333331
    },
    'pound': {
        'milligram': 453592.37,
        'carat': 2267.96185,
        'gram': 453.59237,
        'kilogram': 0.45359237,
        'tonne': 4.5359237E-4,
        'ounce': 16,
        'troy ounce': 14.583333333333
    },
    'troy ounce': {
        'milligram': 3.110348e+4,
        'carat': 155.51857669398,
        'gram': 31.1034768,
        'kilogram': 0.0311034768,
        'tonne': 3.11034768e-5,
        'ounce': 1.0971428571429,
        'pound': 0.0685714285714285714285714285714
    }
}


# Define the conversion function
def convert_mass(value, from_unit, to_unit):
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

result = convert_mass(value, from_unit, to_unit)
print(f'{value} {from_unit} = {result:,.4f} {to_unit}')



# ref: https://www.convert-measurement-units.com/conversion-calculator.php?type=masse