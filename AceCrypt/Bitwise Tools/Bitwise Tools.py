
class BitwiseTools:
    def __init__(self):
        pass

    @staticmethod
    def __decimal_to_bin_oct_hex(decimal: float):
        try:
            binary = f"{decimal:#b}"
            octal = f"{decimal:#o}"
            hexadecimal = f"{decimal:#x}"
            hex_cap = f"{decimal:#X}"
            scientific_notation = f"{decimal:#e}"
            sci_not_cap = f"{decimal:#E}"

            return binary, octal, hexadecimal, hex_cap, scientific_notation, sci_not_cap

        except ValueError as ve:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{ve}\033[0m"

    @staticmethod
    def decimal_to_bin_oct_hex(decimal: float):
        return BitwiseTools.__decimal_to_bin_oct_hex(decimal)

    @staticmethod
    def __binary_to_dec(binary: int):
        try:
            return int(binary, 2)
        except ValueError as ve:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{ve}\033[0m")
            return None

    @staticmethod
    def binary_to_dec(binary: int):
        return BitwiseTools.__binary_to_dec(binary)

    @staticmethod
    def __octal_to_dec(octal: int):
        try:
            return int(octal, 8)
        except ValueError as ve:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{ve}\033[0m")
            return None

    @staticmethod
    def octal_to_dec(octal: int):
        return BitwiseTools.__octal_to_dec(octal)

    @staticmethod
    def __hexadecimal_to_dec(hexadecimal):
        try:
            return int(hexadecimal, 16)
        except ValueError as ve:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{ve}\033[0m")
            return None

    @staticmethod
    def hexadecimal_to_dec(hexadecimal):
        return BitwiseTools.__hexadecimal_to_dec(hexadecimal)

    @staticmethod
    def __bitwise(operand_1: float, operand_2: float):
        try:
            ampersand = operand_1 & operand_2   # and
            bar = operand_1 | operand_2         # or
            caret = operand_1 ^ operand_2       # xor

            tilde_op1 = ~operand_1    # not operand_1
            tilde_op2 = ~operand_2    # not operand_2

            div_op1 = operand_1 >> operand_2    # shift op_1
            div_op2 = operand_2 >> operand_1    # shift op_2
            mul_op1 = operand_1 << operand_2
            mul_op2 = operand_2 << operand_1

            return ampersand, bar, caret, tilde_op1, tilde_op2, div_op1, div_op2, mul_op1, mul_op2

        except ValueError as ve:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{ve}\033[0m"

    @staticmethod
    def bitwise(operand_1: float, operand_2: float):
        return BitwiseTools.__bitwise(operand_1, operand_2)

    @staticmethod
    def __run():
        try:
            while True:
                print("\nOperations:")
                print("\n 1. Decimal\n 2. Binary")
                print(" 3. Octal\n 4. Hexadecimal")
                print(" 5. Bitwise\n 0. Exit")

                choice = input("\nAction: ").lower()

                if choice == "1":
                    while True:
                        decimal = input("\n\nDecimal: ")

                        if decimal == "":
                            break

                        decimal = int(decimal)
                        binary, octal, hexadecimal, hex_cap, scientific_notation, sci_not_cap = BitwiseTools.__decimal_to_bin_oct_hex(decimal)

                        print(f"\nBinary - {binary}")
                        print(f"Octal - {octal}")
                        print(f"Hexadecimal - {hexadecimal}")
                        print(f"Hexadecimal - {hex_cap}")
                        print(f"\nScientific Notation - {scientific_notation}")
                        print(f"Scientific Notation - {sci_not_cap}")


                elif choice == "2":
                    while True:
                        binary = input("\nBinary: ")

                        if binary == "":
                            break

                        decimal = BitwiseTools.__binary_to_dec(binary)
                        binary, octal, hexadecimal, hex_cap, scientific_notation, sci_not_cap = BitwiseTools.decimal_to_bin_oct_hex(decimal)

                        print(f"\nDecimal - {decimal}")
                        print(f"Octal - {octal}")
                        print(f"Hexadecimal - {hexadecimal}")
                        print(f"Hexadecimal - {hex_cap}")
                        print(f"\nScientific Notation - {scientific_notation}")
                        print(f"Scientific Notation - {sci_not_cap}")


                elif choice == "3":
                    while True:
                        octal = input("\nOctal: ")

                        if octal == "":
                            break

                        decimal = BitwiseTools.__octal_to_dec(octal)
                        binary, octal, hexadecimal, hex_cap, scientific_notation, sci_not_cap = BitwiseTools.decimal_to_bin_oct_hex(decimal)

                        print(f"\nDecimal - {decimal}")
                        print(f"Binary - {binary}")
                        print(f"Hexadecimal - {hexadecimal}")
                        print(f"Hexadecimal - {hex_cap}")
                        print(f"\nScientific Notation - {scientific_notation}")
                        print(f"Scientific Notation - {sci_not_cap}")


                elif choice == "4":
                    while True:
                        hexadecimal = input("\nHexadecimal: ")

                        if hexadecimal == "":
                            break

                        decimal = BitwiseTools.__hexadecimal_to_dec(hexadecimal)
                        binary, octal, hexadecimal, hex_cap, scientific_notation, sci_not_cap = BitwiseTools.decimal_to_bin_oct_hex(decimal)

                        print(f"\nDecimal - {decimal}")
                        print(f"Binary - {binary}")
                        print(f"Octal - {octal}")
                        print(f"\nScientific Notation - {scientific_notation}")
                        print(f"Scientific Notation - {sci_not_cap}")


                elif choice == "5":
                    while True:
                        operand_1 = int(input("Operand X: "))
                        operand_2 = int(input("Operand Y: "))

                        ampersand, bar, caret, tilde_op1, tilde_op2, div_op1, div_op2, mul_op1, mul_op2 = BitwiseTools.__bitwise(operand_1, operand_2)

                        print("\n-----------------------------------------")
                        print("                 RESULTS                 ")
                        print("-----------------------------------------")
                        print(f" Ampersand        x & y:  {ampersand}")
                        print(f" Bar              x | y:  {bar}")
                        print(f" Caret            x ^ y:  {caret}")
                        print(f" Total Sum of all above:  {ampersand + bar + caret}")
                        print(f"\n Tilde               ~x:  {tilde_op1}")
                        print(f" Tilde               ~y:  {tilde_op2}")
                        print(f"\n Division        x >> y:  {div_op1}")
                        print(f" Divison         y >> x:  {div_op2}")
                        print(f" Multiplication  x << y:  {mul_op1}")
                        print(f" Multiplication  y << x:  {mul_op2}")
                        print("-----------------------------------------\n\n")

                        while True:
                            choice = input("\nDo you wish to continue? (y/n): ").lower()
                            if choice == "y":
                                break
                            elif choice == "n":
                                break
                            else:
                                print("Invalid input. Please enter 'y' or 'n'.")
                        
                        if choice == "n":
                            break


                elif choice == "0" or choice == "":
                    break

                else:
                    print("\nInvalid input. Please try again.\n\n")


        except ValueError as ve:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{ve}\033[0m"
        
        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    @staticmethod
    def run():
        return BitwiseTools.__run()


if __name__ == "__main__":
    bitwise_tools = BitwiseTools()
    bitwise_tools.run()