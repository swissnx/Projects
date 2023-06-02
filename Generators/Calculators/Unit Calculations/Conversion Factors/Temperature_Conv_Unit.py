
# Celsius to Fahrenheit: F = (C * 9/5) + 32
# Celsius to Kelvin:     K = C + 273.15
# Fahrenheit to Celsius: C = (F - 32) * 5/9
# Fahrenheit to Kelvin:  K = (F + 459.67) * 5/9

CONVERSION_FACTORS = {
  'kelvin': {           # K
    'celsius': 1,       # °C = K - 273.15
    'fahrenheit': 1.8,  # °F = (K * 9/5) - 459.67
  },
  'celsius': {
    'fahrenheit': 1.8,  # °F = (C * 9/5) + 32
    'kelvin': 1,        # K = C + 273.15
  },
  'fahrenheit': {
    'celsius': 5/9,     # °C = (F - 32) * 5/9
    'kelvin': 5/9       # K = (F + 459.67) * 5/9
  }
}

# Define the conversion function
def convert_temperature(value, from_unit, to_unit):
  if from_unit == to_unit:
    return value
  else:
    if from_unit == 'celsius' and to_unit == 'fahrenheit':
        return (value * 1.8) + 32
    elif from_unit == 'celsius' and to_unit == 'kelvin':
        return value + 273.15
    elif from_unit == 'fahrenheit' and to_unit == 'celsius':
        return (value - 32) * 5/9
    elif from_unit == 'fahrenheit' and to_unit == 'kelvin':
        return (value + 459.67) * 5/9
    elif from_unit == 'kelvin' and to_unit == 'celsius':
        return value - 273.15
    elif from_unit == 'kelvin' and to_unit == 'fahrenheit':
        return (value * 9/5) - 459.67
    else:
        return None

# Test the function
print("\nChoose from:")

for i in CONVERSION_FACTORS.keys():
    print(i, end=", ")

from_unit = input("\n\n> ")
to_unit = input("> ")

value = float(input("\n> "))

result = convert_temperature(value, from_unit, to_unit)
if result is not None:
    print(f'{value} {from_unit} = {result:.2f} {to_unit}')
else:
    print(f'Conversion from {from_unit} to {to_unit} is not supported.')
