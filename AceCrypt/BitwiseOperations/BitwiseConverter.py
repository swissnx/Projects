
import time


class BitwiseConverter:
    def __init__(self):
        pass

    @staticmethod
    def __decimal_to_binary_octal_hexadecimal(decimal):
        binary = f"{decimal:#b}"
        octal = f"{decimal:#o}"
        hexadecimal = f"{decimal:#x}"
        hexadecimal_upper = f"{decimal:#X}"
        scientific_notation = f"{decimal:#e}"
        scientific_notation_upper = f"{decimal:#E}"
        return binary, octal, hexadecimal, hexadecimal_upper, scientific_notation, scientific_notation_upper

    @staticmethod
    def decimal_to_binary_octal_hexadecimal(decimal):
        return BitwiseConverter.__decimal_to_binary_octal_hexadecimal(decimal)

    @staticmethod
    def __binary_to_decimal(binary):
        try:
            return int(binary, 2)
        except ValueError as ve:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200mInvalid binary number ({ve})\u001b[0m")
            return None

    @staticmethod
    def binary_to_decimal(binary):
        return BitwiseConverter.__binary_to_decimal(binary)

    @staticmethod
    def __octal_to_decimal(octal):
        try:
            return int(octal, 8)
        except ValueError as ve:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200mInvalid octal number ({ve})\u001b[0m")
            return None

    @staticmethod
    def octal_to_decimal(octal):
        return BitwiseConverter.__octal_to_decimal(octal)

    @staticmethod
    def __hexadecimal_to_decimal(hexadecimal):
        try:
            return int(hexadecimal, 16)
        except ValueError as ve:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200mInvalid hexadecimal number ({ve})\u001b[0m")
            return None

    @staticmethod
    def hexadecimal_to_decimal(hexadecimal):
        return BitwiseConverter.__hexadecimal_to_decimal(hexadecimal)

    @staticmethod
    def __bitwise_operations(value_1, value_2):
        ampersand = value_1 & value_2
        bar = value_1 | value_2
        caret = value_1 ^ value_2
        tilde_v1 = ~value_1
        tilde_v2 = ~value_2
        div_v1 = value_1 >> value_2
        div_v2 = value_2 >> value_1
        mul_v1 = value_1 << value_2
        mul_v2 = value_2 << value_1
        return ampersand, bar, caret, tilde_v1, tilde_v2, div_v1, div_v2, mul_v1, mul_v2

    @staticmethod
    def bitwise_operations(value_1, value_2):
        return BitwiseConverter.__bitwise_operations(value_1, value_2)

    @staticmethod
    def __run():
        while True:
            try:
                print("\n▲▼▲▼▲ Choose from the Operation Below ▲▼▲▼▲")
                print("\n 1. Decimal     --> Binary, Octal, Hexadecimal")
                print(" 2. Binary      --> Decimal\n 3. Octal       --> Decimal\n 4. Hexadecimal --> Decimal")
                print(" 5. Bitwise Operations\n 6. Exit")
                choice = input("\n Choice: ").lower()
                if choice == "1":
                    decimal = input("\n\n>> Decimal: ")
                    while True:
                        if decimal == "":
                            print("\nFinished here. Returning to the main menu... ->")
                            time.sleep(0.5)
                            break
                        decimal = int(decimal)
                        binary, octal, hexadecimal, hexadecimal_upper, scientific_notation, scientific_notation_upper = BitwiseConverter.__decimal_to_binary_octal_hexadecimal(decimal)
                        print(f"\n Binary - {binary}")
                        print(f" Octal - {octal}")
                        print(f" Hexadecimal - {hexadecimal}")
                        print(f" Hexadecimal - {hexadecimal_upper}")
                        print(f"\nScientific Notation - {scientific_notation} | {scientific_notation_upper}")
                        time.sleep(0.5)
                        decimal = input("\n------------------------\n\n>> Enter Decimal: ")

                elif choice == "2":
                    print("\n\nConverts Binary -> Decimal.")
                    binary = input("\n>> Enter Binary: ")
                    while True:
                        if binary == "":
                            print("\nReturning to the Functions menu...")
                            time.sleep(0.5)
                            break
                        decimal = BitwiseConverter.__binary_to_decimal(binary)
                        print(f">> Answer - {decimal}")
                        binary = input("\n>> Enter Binary: ")

                elif choice == "3":
                    print("\n\nConverts Octal -> Decimal.")
                    octal = input("\n>> Enter Octal: ")
                    while True:
                        if octal == "":
                            print("\nReturning to the Functions menu...")
                            time.sleep(0.5)
                            break
                        decimal = BitwiseConverter.__octal_to_decimal(octal)
                        print(f">> Answer - {decimal}")
                        octal = input("\n>> Enter Octal: ")

                elif choice == "4":
                    print("\n\nConverts Hexadecimal -> Decimal.")
                    hexadecimal = input("\n>> Enter Hexadecimal: ")
                    while True:
                        if hexadecimal == "":
                            print("\nReturning to the Functions menu...")
                            time.sleep(0.5)
                            break
                        decimal = BitwiseConverter.__hexadecimal_to_decimal(hexadecimal)
                        print(f">> Answer - {decimal}")
                        hexadecimal = input("\n>> Enter Hexadecimal: ")

                elif choice == "5":
                    while True:
                        print("\n\n▼▼▼ Calculation of Bitwise Operations ▼▼▼\n")

                        value_1 = int(input("Value X: "))
                        value_2 = int(input("Value Y: "))
                        ampersand, bar, caret, tilde_v1, tilde_v2, div_v1, div_v2, mul_v1, mul_v2 = BitwiseConverter.__bitwise_operations(value_1, value_2)

                        print("\n-----------------------------------------")
                        print("                 RESULTS                 ")
                        print("-----------------------------------------")
                        print(f" Ampersand        x & y:  {ampersand}")
                        print(f" Bar              x | y:  {bar}")
                        print(f" Caret            x ^ y:  {caret}")
                        print(f" Total Sum of   (& | ^):  {ampersand + bar + caret}")
                        print(f"\n Tilde               ~x:  {tilde_v1}")
                        print(f" Tilde               ~y:  {tilde_v2}")
                        print(f"\n Division        x >> y:  {div_v1}")
                        print(f" Divison         y >> x:  {div_v2}")
                        print(f" Multiplication  x << y:  {mul_v1}")
                        print(f" Multiplication  y << x:  {mul_v2}")
                        print("-----------------------------------------\n\n")

                        time.sleep(0.5)
                        choice = input("Do you wish to continue? (y/n): ")
                        if choice.lower() != "y":
                            time.sleep(2)
                            print("\n\n")
                            break
                        time.sleep(0.5)

                elif choice == "6" or choice == "":
                    print("\n\nExiting the program...")
                    time.sleep(0.5)
                    print("\nThanks, have a good one!")
                    break
                else:
                    print("\nInvalid input. Please try again.\n\n")
                    time.sleep(0.5)
            except Exception as e:
                print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

    @staticmethod
    def run():
        return BitwiseConverter.__run()


if __name__ == "__main__":
    bit_converter = BitwiseConverter()
    bit_converter.run()
