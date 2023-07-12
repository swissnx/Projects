
import base64
import binascii
import codecs


class ASCIIDecoder:
    def __init__(self):
        pass

    @staticmethod
    def ascii_dec(message):
        try:
            return ''.join(chr(int(x)) for x in message.split())
        except ValueError:
            return None

    @staticmethod
    def binary_dec(message):
        try:
            return ''.join(chr(int(x, 2)) for x in message.split())
        except ValueError:
            return None

    @staticmethod
    def octal_dec(message):
        try:
            return ''.join(chr(int(x, 8)) for x in message.split())
        except ValueError:
            return None

    @staticmethod
    def hex_dec(message):
        try:
            return codecs.decode(message, 'hex').decode()
        except binascii.Error:
            return None

    @staticmethod
    def base64_dec(message):
        try:
            return base64.b64decode(message).decode()
        except binascii.Error:
            return None

    @staticmethod
    def __run():
        try:
            while True:
                print("\nDecode Value:")

                message = ""

                while True:
                    line = input()
                    if line == "END":
                        break
                    message += line + "\n"
                message = message[:-1]

                if message == "":
                    break

                print("\n1. ASCII\n2. Binary\n3. Octal\n4. Hexadecimal\n5. Base64")
                choice = input("\nChoice: ")

                if choice == "1":
                    ascii_dec = ASCIIDecoder.ascii_dec(message)
                    print(f"\nASCII: {ascii_dec}")

                elif choice == "2":
                    binary_dec = ASCIIDecoder.binary_dec(message)
                    print(f"\nBinary: {binary_dec}")

                elif choice == "3":
                    octal_dec = ASCIIDecoder.octal_dec(message)
                    print(f"\nOctal: {octal_dec}")

                elif choice == "4":
                    hex_dec = ASCIIDecoder.hex_dec(message)
                    print(f"\nHexadecimal: {hex_dec}")
                    
                elif choice == "5":
                    base64_dec = ASCIIDecoder.base64_dec(message)
                    print(f"\nBase64: {base64_dec}\n")

        except ValueError as ve:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{ve}\033[0m"

        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    @staticmethod
    def run():
        return ASCIIDecoder.__run()


if __name__ == "__main__":
    ascii_dec = ASCIIDecoder()
    ascii_dec.run()