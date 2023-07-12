
""" SI (1000 based) vs IEC 80000-13 (1024 based)
    They are simply different systems of measurement with different use cases.

IN DECIMAL UNITS:
    The SI (1000-based) system is the international standard for measuring units of data storage and data transfer rates.
    It is commonly used in marketing and advertising for computer hardware and software products.
    SI stands for "Système International d'Unités" which is the International System of Units.
    This system is based on powers of 10, and uses units such as kilo (10^3), mega (10^6), and giga (10^9).

IN BINARY UNITS:
    The IEC 80000-13 (1024-based) system is often used in computer science and information technology, particularly for specifying
    the size of memory and storage devices in binary multiples (kilobyte, megabyte, gigabyte, etc.). IEC 80000-13 is an international standard
    developed by the International Electrotechnical Commission (IEC) for expressing units of digital information using binary prefixes.
    This system is based on powers of 2, and uses units such as kibi (2^10), mebi (2^20), and gibi (2^30).

WHICH ONE IS THE MOST STANDARDIZED?
    The SI (1000-based) units are the official standard adopted by the International System of Units (SI) and are used by many organizations,
    including the International Electrotechnical Commission (IEC) and the Institute of Electrical and Electronics Engineers (IEEE).
    However, the 1024-based units are still commonly used in computing and storage industries.
    In general, the context and the industry in which the units are being used will determine which set of units is appropriate. """


CONVERSION_FACTORS = {
    'b/s': {                # Bit      per second  - SI (1000 based)
        'B/s': 0.125,       # Byte     per second  - SI (1000 based)
        'kb/s': 0.001,      # Kilobit  per second  - SI (1000 based)
        'kB/s': 1.25E-4,    # Kilobyte per second  - SI (1000 based)
        'Mb/s': 1.E-6,      # Megabit  per second  - SI (1000 based)
        'MB/s': 1.25E-7,    # Megabyte per second  - SI (1000 based)
        'Gb/s': 1.E-9,      # Gigabit  per second  - SI (1000 based)
        'GB/s': 1.25E-10,   # Gigabyte per second  - SI (1000 based)
        'Tb/s': 1.E-12,     # Terabit  per second  - SI (1000 based)
        'TB/s': 1.25E-13,   # Terabyte per second  - SI (1000 based)
        'Kib/s': 9.765625E-4,                          # Kibibit  per second  - IEC 80000-13 (1024-based)
        'KiB/s': 1.220703125E-4,                       # Kibibyte per second  - IEC 80000-13 (1024-based)
        'Mib/s': 9.5367431640625E-7,                   # Mebibit  per second  - IEC 80000-13 (1024-based)
        'MiB/s': 1.1920928955078125E-7,                # Mebibyte per second  - IEC 80000-13 (1024-based)
        'Gib/s': 9.31322574615478515625E-10,           # Gbibit   per second  - IEC 80000-13 (1024-based)
        'GiB/s': 1.16415321826934814453125E-10,        # Gbibyte  per second  - IEC 80000-13 (1024-based)
        'Tib/s': 9.094947017729282379150390625E-13,    # Tebibit  per second  - IEC 80000-13 (1024-based)
        'TiB/s': 1.13686837721616029739379882813E-13   # Tebibyte per second  - IEC 80000-13 (1024-based)
    },
    'B/s': {
        'b/s': 8,
        'kb/s': 0.008,
        'kB/s': 0.001,
        'Mb/s': 8.E-6,
        'MB/s': 1e-6,
        'Gb/s': 8e-9,
        'GB/s': 1e-9,
        'Tb/s': 8e-12,
        'TB/s': 1e-12,
        'Kib/s': 0.0078125,
        'KiB/s': 9.765625E-4,
        'Mib/s': 7.62939453125E-6,
        'MiB/s': 9.5367431640625E-7,
        'Gib/s': 7.450580596923828125E-9,
        'GiB/s': 9.31322574615478515625E-10,
        'Tib/s': 7.2759576141834259033203125E-12,
        'TiB/s': 9.094947017729282379150390625E-13
    },
    'kb/s': {
        'b/s': 1000,
        'B/s': 125,
        'kB/s': 0.125,
        'Mb/s': 0.001,
        'MB/s': 1.25E-4,
        'Gb/s': 1e-6,
        'GB/s': 1.25e-7,
        'Tb/s': 1e-9,
        'TB/s': 1.25e-10,
        'Kib/s': 0.9765625,
        'KiB/s': 0.1220703125,
        'Mib/s': 9.5367431640625E-4,
        'MiB/s': 1.1920928955078125E-4,
        'Gib/s': 9.31322574615478515625E-7,
        'GiB/s': 1.16415321826934814453125E-7,
        'Tib/s': 9.094947017729282379150390625E-10,
        'TiB/s': 1.13686837721616029739379882813E-10
    },
    'kB/s': {
        'b/s': 8000,
        'B/s': 1000,
        'kb/s': 8,
        'Mb/s': 0.008,
        'MB/s': 0.001,
        'Gb/s': 8e-6,
        'GB/s': 1e-6,
        'Tb/s': 8e-9,
        'TB/s': 1e-9,
        'Kib/s': 7.8125,
        'KiB/s': 0.9765625,
        'Mib/s': 0.00762939453125,
        'MiB/s': 9.5367431640625E-4,
        'Gib/s': 7.450580596923828125E-6,
        'GiB/s': 9.31322574615478515625E-7,
        'Tib/s': 7.2759576141834259033203125E-9,
        'TiB/s': 9.094947017729282379150390625E-10
    },
    'Mb/s': {
        'b/s': 1000000,
        'B/s': 125000,
        'kb/s': 1000,
        'kB/s': 125,
        'MB/s': 0.125,
        'Gb/s': 0.001,
        'GB/s': 1.25E-4,
        'Tb/s': 1e-6,
        'TB/s': 1.25e-7,
        'Kib/s': 976.5625,
        'KiB/s': 122.0703125,
        'Mib/s': 0.95367431640625,
        'MiB/s': 0.11920928955078125,
        'Gib/s': 9.31322574615478515625E-4,
        'GiB/s': 1.16415321826934814453125E-4,
        'Tib/s': 9.094947017729282379150390625E-7,
        'TiB/s': 1.13686837721616029739379882813E-7
    },
    'MB/s': {
        'b/s': 8000000,
        'B/s': 1000000,
        'kb/s': 8000,
        'kB/s': 1000,
        'Mb/s': 8,
        'Gb/s': 0.008,
        'GB/s': 0.001,
        'Tb/s': 8e-6,
        'TB/s': 1e-6,
        'Kib/s': 7812.5,
        'KiB/s': 976.5625,
        'Mib/s': 7.62939453125,
        'MiB/s': 0.95367431640625,
        'Gib/s': 0.007450580596923828125,
        'GiB/s': 9.31322574615478515625E-4,
        'Tib/s': 7.2759576141834259033203125E-6,
        'TiB/s': 9.094947017729282379150390625E-7
    },
    'Gb/s': {
        'b/s': 1000000000,
        'B/s': 125000000,
        'kb/s': 1000000,
        'kB/s': 125000,
        'Mb/s': 1000,
        'MB/s': 125,
        'GB/s': 0.125,
        'Tb/s': 0.001,
        'TB/s': 1.25E-4,
        'Kib/s': 976562.5,
        'KiB/s': 122070.3125,
        'Mib/s': 953.67431640625,
        'MiB/s': 119.20928955078125,
        'Gib/s': 0.931322574615478515625,
        'GiB/s': 0.116415321826934814453125,
        'Tib/s': 9.094947017729282379150390625E-4,
        'TiB/s': 1.13686837721616029739379882813E-4
    },
    'GB/s': {
        'b/s': 8000000000,
        'B/s': 1000000000,
        'kb/s': 8000000,
        'kB/s': 1000000,
        'Mb/s': 8000,
        'MB/s': 1000,
        'Gb/s': 8,
        'Tb/s': 0.008,
        'TB/s': 0.001,
        'Kib/s': 7812500,
        'KiB/s': 976562.5,
        'Mib/s': 7629.39453125,
        'MiB/s': 953.67431640625,
        'Gib/s': 7.450580596923828125,
        'GiB/s': 0.931322574615478515625,
        'Tib/s': 0.0072759576141834259033203125,
        'TiB/s': 9.094947017729282379150390625E-4
    },
    'Tb/s': {
        'b/s': 1000000000000,
        'B/s': 125000000000,
        'kb/s': 1000000000,
        'kB/s': 125000000,
        'Mb/s': 1000000,
        'MB/s': 125000,
        'Gb/s': 1000,
        'GB/s': 125,
        'TB/s': 0.125,
        'Kib/s': 976562500,
        'KiB/s': 122070312.5,
        'Mib/s': 953674.31640625,
        'MiB/s': 119209.28955078125,
        'Gib/s': 931.322574615478515625,
        'GiB/s': 116.415321826934814453125,
        'Tib/s': 0.9094947017729282379150390625,
        'TiB/s': 0.113686837721616029739379882813
    },
    'TB/s': {
        'b/s': 8000000000000,
        'B/s': 1000000000000,
        'kb/s': 8000000000,
        'kB/s': 1000000000,
        'Mb/s': 8000000,
        'MB/s': 1000000,
        'Gb/s': 8000,
        'GB/s': 1000,
        'Tb/s': 8,
        'Kib/s': 7812500000,
        'KiB/s': 976562500,
        'Mib/s': 7629394.53125,
        'MiB/s': 953674.31640625,
        'Gib/s': 7450.580596923828125,
        'GiB/s': 931.322574615478515625,
        'Tib/s': 7.2759576141834259033203125,
        'TiB/s': 0.9094947017729282379150390625
    },
    'Kib/s': {
        'b/s': 1024,
        'B/s': 128,
        'kb/s': 1.024,
        'kB/s': 0.128,
        'Mb/s': 0.001024,
        'MB/s': 1.28E-4,
        'Gb/s': 1.024E-6,
        'GB/s': 1.28E-7,
        'Tb/s': 1.024E-9,
        'TB/s': 1.28E-10,
        'KiB/s': 0.125,
        'Mib/s': 9.765625E-4,
        'MiB/s': 1.220703125E-4,
        'Gib/s': 9.5367431640625E-7,
        'GiB/s': 1.1920928955078125E-7,
        'Tib/s': 9.31322574615478515625E-10,
        'TiB/s': 1.16415321826934814453125E-10
    },
    'KiB/s': {
        'b/s': 8192,
        'B/s': 1024,
        'kb/s': 8.192,
        'kB/s': 1.024,
        'Mb/s': 0.008192,
        'MB/s': 0.001024,
        'Gb/s': 8.192E-6,
        'GB/s': 1.024E-6,
        'Tb/s': 8.192E-9,
        'TB/s': 1.024E-9,
        'Kib/s': 8,
        'Mib/s': 0.0078125,
        'MiB/s': 9.765625E-4,
        'Gib/s': 7.62939453125E-6,
        'GiB/s': 9.5367431640625E-7,
        'Tib/s': 7.450580596923828125E-9,
        'TiB/s': 9.31322574615478515625E-10
    },
    'Mib/s': {
        'b/s': 1048576,
        'B/s': 131072,
        'kb/s': 1048.576,
        'kB/s': 131.072,
        'Mb/s': 1.048576,
        'MB/s': 0.131072,
        'Gb/s': 0.001048576,
        'GB/s': 1.31072E-4,
        'Tb/s': 1.048576E-6,
        'TB/s': 1.31072E-7,
        'Kib/s': 1024,
        'KiB/s': 128,
        'MiB/s': 0.125,
        'Gib/s': 9.765625E-4,
        'GiB/s': 1.220703125E-4,
        'Tib/s': 9.5367431640625E-7,
        'TiB/s': 1.1920928955078125E-7
    },
    'MiB/s': {
        'b/s': 8388608,
        'B/s': 1048576,
        'kb/s': 8388.608,
        'kB/s': 1048.576,
        'Mb/s': 8.388608,
        'MB/s': 1.048576,
        'Gb/s': 0.008388608,
        'GB/s': 0.001048576,
        'Tb/s': 8.388608E-6,
        'TB/s': 1.048576E-6,
        'Kib/s': 8192,
        'KiB/s': 1024,
        'Mib/s': 8,
        'Gib/s': 0.0078125,
        'GiB/s': 9.765625E-4,
        'Tib/s': 7.62939453125E-6,
        'TiB/s': 9.5367431640625E-7
    },
    'Gib/s': {
        'b/s': 1073741824,
        'B/s': 134217728,
        'kb/s': 1073741.824,
        'kB/s': 134217.728,
        'Mb/s': 1073.741824,
        'MB/s': 134.217728,
        'Gb/s': 1.073741824,
        'GB/s': 0.134217728,
        'Tb/s': 0.001073741824,
        'TB/s': 1.34217728E-4,
        'Kib/s': 1048576,
        'KiB/s': 131072,
        'Mib/s': 1024,
        'MiB/s': 128,
        'GiB/s': 0.125,
        'Tib/s': 9.765625E-4,
        'TiB/s': 1.220703125E-4
    },
    'GiB/s': {
        'b/s': 8589934592,
        'B/s': 1073741824,
        'kb/s': 8589934.592,
        'kB/s': 1073741.824,
        'Mb/s': 8589.934592,
        'MB/s': 1073.741824,
        'Gb/s': 8.589934592,
        'GB/s': 1.073741824,
        'Tb/s': 0.008589934592,
        'TB/s': 0.001073741824,
        'Kib/s': 8388608,
        'KiB/s': 1048576,
        'Mib/s': 8192,
        'MiB/s': 1024,
        'Gib/s': 8,
        'Tib/s': 0.0078125,
        'TiB/s': 9.765625E-4
    },
    'Tib/s': {
        'b/s': 1099511627776,
        'B/s': 137438953472,
        'kb/s': 1099511627.776,
        'kB/s': 137438953.472,
        'Mb/s': 1099511.627776,
        'MB/s': 137438.953472,
        'Gb/s': 1099.511627776,
        'GB/s': 137.438953472,
        'Tb/s': 1.099511627776,
        'TB/s': 0.137438953472,
        'Kib/s': 1073741824,
        'KiB/s': 134217728,
        'Mib/s': 1048576,
        'MiB/s': 131072,
        'Gib/s': 1024,
        'GiB/s': 128,
        'TiB/s': 0.125,
    },
    'TiB/s': {
        'b/s': 8796093022208,
        'B/s': 1099511627776,
        'kb/s': 8796093022.208,
        'kB/s': 1099511627.776,
        'Mb/s': 8796093.022208,
        'MB/s': 1099511.627776,
        'Gb/s': 8796.093022208,
        'GB/s': 1099.511627776,
        'Tb/s': 8.796093022208,
        'TB/s': 1.099511627776,
        'Kib/s': 8589934592,
        'KiB/s': 1073741824,
        'Mib/s': 8388608,
        'MiB/s': 1048576,
        'Gib/s': 8192,
        'GiB/s': 1024,
        'Tib/s': 8,
    }
}


# Define the conversion function
def convert_transfer_rate(value, from_unit, to_unit):
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

result = convert_transfer_rate(value, from_unit, to_unit)
print(f'{value} {from_unit} = {result:,.2f} {to_unit}')





# REFERENCE: https://keisan.casio.com/exec/system/1227620183