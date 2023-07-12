
CONVERSION_FACTORS = {
    'liter': {                                           # l      - metric
        'cubic millimeter': 1000000,                     # mm3    - metric
        'cubic centimeter': 1000,                        # cm3    - metric
        'cubic meter': 0.001,                            # m3     - metric
        'gallon': 0.219969248299087787527303682945,      # gal    - imperial
        'barrel': 0.00611025689719688298686954674848,    # bl     - imperial
        'gallon-flu': 0.264172052358148415379899921609,   # U.S. fluid gallon
        'barrel-flu': 0.00838641436057614017079047370188,
        'gallon-dry': 0.227020746067213972908573699619,   # U.S. dry gallon
        'barrel-dry': 0.00864840937398910372985042665214,
        'petroleum barrel': 0.00628981077043210512809285527641,  # petroleum barrel
    },
    'cubic millimeter': {
        'liter': 1.E-6,
        'cubic centimeter': 0.001,
        'cubic meter': 1.E-9,
        'gallon': 2.19969248e-7,
        'barrel': 6.110256897e-9,
        'gallon-flu': 2.64172052358148415379899921609E-7,   # U.S. fluid gallon
        'barrel-flu': 8.38641436057614017079047370188E-9,
        'gallon-dry': 2.27020746067213972908573699619E-7,   # U.S. dry gallon
        'barrel-dry': 8.64840937398910372985042665214E-9,
        'petroleum barrel': 6.28981077043210512809285527641E-9,  # petroleum barrel
    },
    'cubic centimeter': {
        'liter': 0.001,
        'cubic millimeter': 1000,
        'cubic meter': 1.E-6,
        'gallon': 2.19969248299087787527303682945E-4,
        'barrel': 6.11025689719688298686954674848E-6,
        'gallon-flu': 2.64172052358148415379899921609E-4,   # U.S. fluid gallon
        'barrel-flu': 8.38641436057614017079047370188E-6,
        'gallon-dry': 2.27020746067213972908573699619E-4,   # U.S. dry gallon
        'barrel-dry': 8.64840937398910372985042665214E-6,
        'petroleum barrel': 6.28981077043210512809285527641E-6,  # petroleum barrel
    },
    'cubic meter': {
        'liter': 1000,
        'cubic millimeter': 1000000000,
        'cubic centimeter': 1000000,
        'gallon': 219.969248299087787527303682945,
        'barrel': 6.11025689719688298686954674848,
        'gallon-flu': 264.172052358148415379899921609,   # U.S. fluid gallon
        'barrel-flu': 8.38641436057614017079047370188,
        'gallon-dry': 227.020746067213972908573699619,   # U.S. dry gallon
        'barrel-dry': 8.64840937398910372985042665214,
        'petroleum barrel': 6.28981077043210512809285527641,  # petroleum barrel
    },
    'gallon': {
        'liter': 4.54609,
        'cubic millimeter': 4546090,
        'cubic centimeter': 4546.09,
        'cubic meter': 0.00454609,
        'barrel': 0.0277777777777777777777777777778,
        'gallon-flu': 1.20094992550485492967440923463,   # U.S. fluid gallon
        'barrel-flu': 0.0381253944604715850690288645914,
        'gallon-dry': 1.0320567434887007700999378101,    # U.S. dry gallon
        'barrel-dry': 0.039316447370998124575235726099,
        'petroleum barrel': 0.0285940458453536888017716484435,  # petroleum barrel
    },
    'barrel': {
        'liter': 163.65924,
        'cubic millimeter': 163659240,
        'cubic centimeter': 163659.24,
        'cubic meter': 0.16365924,
        'gallon': 36.3687347479,
        'gallon-flu': 43.2341973181747774682787324466,   # U.S. fluid gallon
        'barrel-flu': 1.37251420057697706248503912529,
        'gallon-dry': 37.1540427655932277235977611636,   # U.S. dry gallon
        'barrel-dry': 1.41539210535593248470848613956,
        'petroleum barrel': 1.02938565043273279686377934397,  # petroleum barrel
    },
    'gallon-flu': {
        'liter': 3.785411784,
        'cubic millimeter': 3785411.784,
        'cubic centimeter': 3785.411784,
        'cubic meter': 0.003785411784,
        'gallon': 0.832674184628988867356343583167,
        'barrel': 0.0231298384619163574265650995324,
        'barrel-flu': 0.031746031746031746031746031746,   # U.S. fluid gallon
        'gallon-dry': 0.859367007375303429097571637169,   # U.S. dry gallon
        'barrel-dry': 0.0327377907571544163465741576064,
        'petroleum barrel': 0.0238095238095238095238095238095,  # petroleum barrel
    },
    'barrel-flu': {
        'liter': 119.240471196,
        'cubic millimeter': 119240471.196,
        'cubic centimeter': 119240.471196,
        'cubic meter': 0.119240471196,
        'gallon': 26.2292368158131493217248228698,
        'barrel': 0.728589911550365258936800635271,
        'gallon-flu': 31.5,                              # U.S. fluid gallon
        'gallon-dry': 27.0700607323220580165735065708,   # U.S. dry gallon
        'barrel-dry': 1.0312404088503641149170859646,
        'petroleum barrel': 0.75,    # petroleum barrel
    },
    'gallon-dry':{
        'liter': 4.40488377086,
        'cubic millimeter': 4404883.77086,
        'cubic centimeter': 4404.88377086,
        'cubic meter': 0.00440488377086,
        'gallon': 0.96893897192092545462144392214,
        'barrel': 0.0269149714422479292950401089483,
        'gallon-flu': 1.16364718614718614718614718615,     # U.S. fluid gallon
        'barrel-flu': 0.0369411805126090840376554662269,
        'barrel-dry': 0.0380952380952380952380952380952,   # U.S. dry gallon
        'petroleum barrel': 0.0277058853844568130282415996702,  # petroleum barrel
    },
    'barrel-dry': {
        'liter': 115.628198985075,
        'cubic millimeter': 115628198.985075,
        'cubic centimeter': 115628.198985075,
        'cubic meter': 0.115628198985075,
        'gallon': 25.4346480129242931838129029562,
        'barrel': 0.706518000359008143994802859893,
        'gallon-flu': 30.5457386363636363636363636364,   # U.S. fluid gallon
        'barrel-flu': 0.969705988455988455988455988456,
        'gallon-dry': 26.25,                             # U.S. dry gallon
        'petroleum barrel': 0.727279491341991341991341991342,  # petroleum barrel
    },
    'petroleum barrel': {
        'liter': 158.987294928,
        'cubic millimeter': 158987294.928,
        'cubic centimeter': 158987.294928,
        'cubic meter': 0.158987294928,
        'gallon': 34.972315754417532428966430493,
        'barrel': 0.971453215400487011915734180362,
        'gallon-flu': 42,                                # U.S. fluid gallon
        'barrel-flu': 1.33333333333333333333333333333,
        'gallon-dry': 36.0934143097627440220980087611,   # U.S. dry gallon
        'barrel-dry': 1.37498721180048548655611461947,
    }
}

# Define the conversion function
def convert_volume(value, from_unit, to_unit):
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

result = convert_volume(value, from_unit, to_unit)
print(f'{value} {from_unit} = {result} {to_unit}')
