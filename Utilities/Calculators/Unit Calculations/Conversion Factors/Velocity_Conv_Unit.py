
CONVERSION_FACTORS = {
    'meter/second': {                                       # m/s
        'kilometer/hour': 3.6,                              # km/h
        'foot/second': 3.28083989501312335958005249344,     # fps
        'foot/minute': 196.850393700787401574803149606,     # fpm
        'foot/hour': 11811.0236220472440944881889764,       # fph
        'mile/second': 6.21371192237333969617434184363E-4,  # mps
        'mile/minute': 0.0372822715342400381770460510618,   # mpm
        'mile/hour': 2.23693629205440229062276306371        # mph
    },
    'kilometer/hour': {
        'meter/second': 0.277777777777777777777777777778,
        'foot/second': 0.9113444152814231554389034704,
        'foot/minute': 54.680664916885389326334208224,
        'foot/hour': 3280.83989501312335958005249344,
        'mile/second': 1.72603108954814991560398384545E-4,
        'mile/minute': 0.0103561865372888994936239030727,
        'mile/hour': 0.621371192237333969617434184363
    },
    'foot/second': {
        'meter/second': 0.3048,
        'kilometer/hour': 1.09728,
        'foot/minute': 60,
        'foot/hour': 3600,
        'mile/second': 1.89393939393939393939393939394E-4,
        'mile/minute': 0.0113636363636363636363636363636,
        'mile/hour': 0.681818181818181818181818181818
    },
    'foot/minute': {
        'meter/second': 0.00508,
        'kilometer/hour': 0.018288,
        'foot/second': 0.0166666666666666666666666666667,
        'foot/hour': 60,
        'mile/second': 3.15656565656565656565656565657E-6,
        'mile/minute': 1.89393939393939393939393939394E-4,
        'mile/hour': 0.0113636363636363636363636363636
    },
    'foot/hour': {
        'meter/second': 8.46666666666666666666666666667E-5,
        'kilometer/hour': 3.048E-4,
        'foot/second': 2.77777777777777777777777777778E-4,
        'foot/minute': 0.0166666666666666666666666666667,
        'mile/second': 5.26094276094276094276094276094E-8,
        'mile/minute': 3.15656565656565656565656565657E-6,
        'mile/hour': 1.89393939393939393939393939394E-4
    },
    'mile/second': {
        'meter/second': 1609.344,
        'kilometer/hour': 5793.6384,
        'foot/second': 5280,
        'foot/minute': 316800,
        'foot/hour': 19008000,
        'mile/minute': 60,
        'mile/hour': 3600
    },
    'mile/minute': {
        'meter/second': 26.8224,
        'kilometer/hour': 96.56064,
        'foot/second': 88,
        'foot/minute': 5280,
        'foot/hour': 316800,
        'mile/second': 0.0166666666666666666666666666667,
        'mile/hour': 60
    },
    'mile/hour': {
        'meter/second': 0.44704,
        'kilometer/hour': 1.609344,
        'foot/second': 1.46666666666666666666666666667,
        'foot/minute': 88,
        'foot/hour': 5280,
        'mile/second': 2.77777777777777777777777777778E-4,
        'mile/minute': 0.0166666666666666666666666666667
    }
}


# Define the conversion function
def convert_velocity(value, from_unit, to_unit):
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

result = convert_velocity(value, from_unit, to_unit)
print(f'{value} {from_unit} = {result} {to_unit}')