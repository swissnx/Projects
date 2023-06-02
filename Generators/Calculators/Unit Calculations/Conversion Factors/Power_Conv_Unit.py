
CONVERSION_FACTORS = {
    'watt': {                 # W
        'kilowatt': 0.001,    # kW
        'dBm': 30,            # dBm (decibel)  (mW = milliWatt)
        'horsepower': 0.00135962161730390432342679032425   # PS (Pferdestärke) / hp (horsepower) - metric
    },
    'kilowatt': {
        'watt': 1000,
        'dBm': 60,
        'horsepower': 1.35962161730390432342679032425
    },
    'dBm': {
        'watt': 0.0012589254117941672104239541064,
        'kilowatt': 1.2589254117941672104239541064E-6,
        'horsepower': 1.71166220444856936932109552381E-6
    },
    'horsepower': {
        'watt': 735.49875,
        'kilowatt': 0.73549875,
        'dBm': 58.6658193896896878234547373262
    }
}

# Define the conversion function
def convert_power(value, from_unit, to_unit):
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

result = convert_power(value, from_unit, to_unit)
print(f'{value} {from_unit} = {result} {to_unit}')
