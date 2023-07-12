
import time

class BitwiseConverter:
    def __init__(self):
        pass

    def decimal_to_binary_octal_hexadecimal(self):
        decimal = input("\n\n>> \u001b[38;5;254mEnter Decimal:\u001b[0m ")
        while True:
            if decimal == "":
              print("\n\u001b[38;5;94;3mFinished here. Returning to the main menu... ->\u001b[0m\n")
              time.sleep(1)
              break
            decimal = int(decimal)
            print(f"\n \u001b[38;5;4mBinary      -\u001b[0m \u001b[38;5;1m{decimal:#b}\u001b[0m")
            print(f" \u001b[38;5;4mOctal       -\u001b[0m \u001b[38;5;1m{decimal:#o}\u001b[0m")
            print(f" \u001b[38;5;4mHexadecimal -\u001b[0m \u001b[38;5;1m{decimal:#x}\u001b[0m")
            print(f" \u001b[38;5;4mHexadecimal -\u001b[0m \u001b[38;5;1m{decimal:#X}\u001b[0m")
            print(f"\n\u001b[38;5;4mScientific notation -\u001b[0m \u001b[38;5;1m{decimal:#e}\u001b[0m | \u001b[38;5;1m{decimal:#E}\u001b[0m")
            time.sleep(1)
            decimal = input("\n\u001b[38;5;209m------------------------\u001b[0m\n\n>> \u001b[38;5;254mEnter Decimal:\u001b[0m ")

    def binary_octal_hexadecimal_to_decimal(self):
        time.sleep(1.5)
        print('\n\n\n\u001b[38;5;14mEnter\u001b[0m "\u001b[38;5;92mbin/binary\u001b[0m" \u001b[38;5;14mor\u001b[0m "\u001b[38;5;207moct/octal\u001b[0m" \u001b[38;5;14mor\u001b[0m "\u001b[38;5;196mhex/hexadecimal\u001b[0m"')
        user = input("\n>> \u001b[38;5;254mChoose function:\u001b[0m ")

        while True:
            if user == "":
              print("\n\u001b[38;5;94;3mFinished here. Returning to the main menu... ->\u001b[0m\n")
              time.sleep(1)
              break
              
            if user == "b".lower() or user == "bin".lower() or user == "binary".lower():
                print("\n\nConverts \u001b[38;5;92mBinary\u001b[0m -> \u001b[38;5;46mDecimal.\u001b[0m")
                binary = input("\n>> Enter \u001b[38;5;92mBinary\u001b[0m: ")
                while True:
                    if binary == "":
                      print("\n\u001b[38;5;94;3mReturning to the Functions menu...\u001b[0m")
                      time.sleep(1)
                      break
                    print(f">> \u001b[38;5;2mAnswer\u001b[0m - \u001b[38;5;4m{int(binary, 2)}\u001b[0m")
                    binary = input("\n>> Enter \u001b[38;5;92mBinary\u001b[0m: ")
                return self.binary_octal_hexadecimal_to_decimal()

            if user == "o".lower() or user == "oct".lower() or user == "octal".lower():
                print("\n\nConverts \u001b[38;5;207mOctal\u001b[0m -> \u001b[38;5;46mDecimal.\u001b[0m")
                octal = input("\n>> Enter \u001b[38;5;207mOctal\u001b[0m: ")
                while True:
                    if octal == "":
                      print("\n\u001b[38;5;94;3mReturning to the Functions menu...\u001b[0m")
                      time.sleep(1)
                      break
                    print(f">> \u001b[38;5;2mAnswer\u001b[0m - \u001b[38;5;4m{int(octal, 8)}\u001b[0m")
                    octal = input("\n>> Enter \u001b[38;5;207mOctal\u001b[0m: ")
                return self.binary_octal_hexadecimal_to_decimal()

            if user == "x".lower() or user == "hex".lower() or user == "hexadecimal".lower():
                print("\n\nConverts \u001b[38;5;196mHexadecimal\u001b[0m -> \u001b[38;5;46mDecimal.\u001b[0m")
                hexadecimal = input("\n>> Enter \u001b[38;5;196mHexadecimal\u001b[0m: ")
                while True:
                    if hexadecimal == "":
                      print("\n\u001b[38;5;94;3mReturning to the Functions menu...\u001b[0m")
                      time.sleep(1)
                      break
                    print(f">> \u001b[38;5;2mAnswer\u001b[0m - \u001b[38;5;4m{int(hexadecimal, 16)}\u001b[0m")
                    hexadecimal = input("\n>> Enter \u001b[38;5;196mHexadecimal\u001b[0m: ")
                return self.binary_octal_hexadecimal_to_decimal()
            else:
                print('\n\u001b[38;5;94;3mInvalid input! Enter \u001b[4m"b" for Binary, "o" for Octal, "x" for Hexadecimal\u001b[0m\n')
            user = input("\n>> \u001b[38;5;254mChoose function:\u001b[0m ")

    def bitwise_operations(self):
      while True:
          print("\n\n\u001b[38;5;226m▼▼▼ Calculation of Bitwise Operations ▼▼▼\n")
          
          a = int(input("\u001b[38;5;254;1mValue A:\u001b[0m "))
          b = int(input("\u001b[38;5;254;1mValue B:\u001b[0m "))
          c = a & b
          d = a | b
          e = a ^ b
          ta = ~a
          tb = ~b
          x = a >> b
          y = b >> a
          z = a << b
          v = b << a
          
          print("\n\u001b[38;5;209m-----------------------------------------\u001b[0m")  # word-green-2
          print("\u001b[38;5;202;1m                 RESULTS                 \u001b[0m")  # sign-red-196
          print("\u001b[38;5;209m-----------------------------------------\u001b[0m\n")  # operands-blue-4
          print(f" \u001b[38;5;2mAmpersand\u001b[0m        \u001b[38;5;4ma\u001b[0m \u001b[38;5;196m&\u001b[0m \u001b[38;5;4mb\u001b[0m:  \u001b[1m{c}\u001b[0m")
          print(f" \u001b[38;5;2mBar\u001b[0m              \u001b[38;5;4ma\u001b[0m \u001b[38;5;196m|\u001b[0m \u001b[38;5;4mb\u001b[0m:  \u001b[1m{d}\u001b[0m")
          print(f" \u001b[38;5;2mCaret\u001b[0m            \u001b[38;5;4ma\u001b[0m \u001b[38;5;196m^\u001b[0m \u001b[38;5;4mb\u001b[0m:  \u001b[1m{e}\u001b[0m")
          print(f" \u001b[38;5;2mTotal Sum of\u001b[0m   \u001b[38;5;4m(\u001b[0m\u001b[38;5;196m& | ^\u001b[0m\u001b[38;5;4m)\u001b[0m:  \u001b[1m{c + d + e}\u001b[0m")
          print("\n")
          print(f" \u001b[38;5;2mTilde\u001b[0m               \u001b[38;5;196m~\u001b[0m\u001b[38;5;4ma\u001b[0m:  \u001b[1m{ta}\u001b[0m")
          print(f" \u001b[38;5;2mTilde\u001b[0m               \u001b[38;5;196m~\u001b[0m\u001b[38;5;4mb\u001b[0m:  \u001b[1m{tb}\u001b[0m")
          print("\n")
          print(f" \u001b[38;5;2mDivision\u001b[0m        \u001b[38;5;4ma\u001b[0m \u001b[38;5;196m>>\u001b[0m \u001b[38;5;4mb\u001b[0m:  \u001b[1m{x}\u001b[0m")
          print(f" \u001b[38;5;2mDivison\u001b[0m         \u001b[38;5;4mb\u001b[0m \u001b[38;5;196m>>\u001b[0m \u001b[38;5;4ma\u001b[0m:  \u001b[1m{y}\u001b[0m")
          print("\n")
          print(f" \u001b[38;5;2mMultiplication\u001b[0m  \u001b[38;5;4ma\u001b[0m \u001b[38;5;196m<<\u001b[0m \u001b[38;5;4mb\u001b[0m:  \u001b[1m{z}\u001b[0m")
          print(f" \u001b[38;5;2mMultiplication\u001b[0m  \u001b[38;5;4mb\u001b[0m \u001b[38;5;196m<<\u001b[0m \u001b[38;5;4ma\u001b[0m:  \u001b[1m{v}\u001b[0m\n")
          print("\u001b[38;5;209m-----------------------------------------\u001b[0m\n\n")

          time.sleep(1)
          choice = input("\u001b[38;5;94;3mDo you wish to continue (y/n)?\u001b[0m ")
          if choice.lower() != "y":
              time.sleep(2)
              print("\n\n")
              break
          time.sleep(1)

    def choice(self):
      while True:
        print("\n\u001b[38;5;208;1m▲▼▲▼▲ Choose The Operation Below ▲▼▲▼▲\u001b[0m")  # orange-208
        print("\n • \u001b[38;5;92mbin\u001b[0m/\u001b[38;5;207moct\u001b[0m/\u001b[38;5;196mhex\u001b[0m \u001b[38;5;14mto Decimal operations\u001b[0m")  # binary: purple-92  octal: pink-207   hex: red-196
        print(" • \u001b[38;5;46mdec\u001b[0m/\u001b[38;5;46mdecimal\u001b[0m \u001b[38;5;14mto Bin/Oct/Hex operations\u001b[0m")   # blue-4
        print(" • \u001b[38;5;226mbit\u001b[0m/\u001b[38;5;226mbitwise\u001b[0m \u001b[38;5;14mfor Bitwise operations\u001b[0m")  # yellow-226
        print(' • \u001b[38;5;94mPress \u001b[4m"Enter"\u001b[0m\u001b[38;5;94m to exit the program\u001b[0m')  # brown-3/11/94
        choice = input("\n\u001b[38;5;48m Enter here:\u001b[0m ").lower()
        if choice == "dec" or choice == "d" or choice == "decimal":
            self.decimal_to_binary_octal_hexadecimal()
        elif choice == "b" or choice == "bin" or choice == "binary":
            self.binary_octal_hexadecimal_to_decimal()
        elif choice == "o" or choice == "oct" or choice == "octal":
            self.binary_octal_hexadecimal_to_decimal()
        elif choice == "x" or choice == "hex" or choice == "hexadecimal":
            self.binary_octal_hexadecimal_to_decimal()
        elif choice == "bit" or choice == "bitwise":
            self.bitwise_operations()
        elif choice == "":
            print("\n\n\u001b[38;5;94;3mExiting the program...\u001b[0m")  # brown-3/11/94
            time.sleep(2)
            print("\n\u001b[38;5;10mThanks, have a good one!\u001b[0m")  # green-10
            break
        else:
            print("\n\u001b[38;5;162;3mInvalid input. Please try again.\u001b[0m\n\n")  # pink-162
            time.sleep(1)


if __name__ == '__main__':
    converter = BitwiseConverter()
    converter.choice()

