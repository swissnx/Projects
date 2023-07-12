
import base64
import binascii


class ASCIIEncoder:
    def __init__(self):
        pass

    @staticmethod
    def __textEnc(message):
        try:
            if message == "":
                raise ValueError("Message cannot be empty")

            ascii_enc = ' '.join(str(ord(char)) for char in message)
            binary_enc = " ".join(format(ord(x), 'b') for x in message)
            octal_enc = " ".join("" + oct(ord(c))[2:] for c in message)
            hex_enc = binascii.hexlify(message.encode()).decode()  #.upper()
            base64_enc = base64.b64encode(message.encode()).decode()

            return ascii_enc, binary_enc, octal_enc, hex_enc, base64_enc

        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    @staticmethod
    def textEnc(message):
        return ASCIIEncoder.__textEnc(message)

    def run(self):
        try:
            while True:
                print("Encode Text:")

                message = ""
                
                while True:
                    line = input()
                    if line == "END":
                        break
                    message += line + "\n"
                # remove the last newline character
                message = message[:-1]    # [:-1] slice notation means “all characters from the start of the string up to, but not including, the last character.”

                if message == "":
                    break

                ascii_enc, binary_enc, octal_enc, hex_enc, base64_enc = self.textEnc(message)

                print(f"\nASCII: {ascii_enc}")
                print(f"Binary: {binary_enc}")
                print(f"Octal: {octal_enc}")
                print(f"Hexadecimal: {hex_enc}")
                print(f"Base64: {base64_enc}\n\n")

        except ValueError as ve:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{ve}\033[0m"

        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"


if __name__ == "__main__":
    ascii_enc = ASCIIEncoder()
    ascii_enc.run()