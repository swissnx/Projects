
import codecs


class Rot13:
    def __init__(self):
        self.__message = ''

    def __encode(self):
        self.__message = input("To Encode: ")
        try:
            return codecs.encode(self.__message, 'rot13')
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

    def __decode(self):
        self.__message = input("To Decode: ")
        try:
            return codecs.decode(self.__message, 'rot13')
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

    def __run(self):
        print("\nWould you like to encode or decode a message?\n1. Encode\n2. Decode")
        prompt = input("\nChoice: ")

        if prompt.lower() == '1':
            encoded_message = self.__encode()
            print(f"Encoded message: {encoded_message}")
        elif prompt.lower() == '2':
            decoded_message = self.__decode()
            print(f"Decoded message: {decoded_message}")
        else:
            print("Invalid prompt. Please enter '1' or '2'")

    def encode(self):
        return self.__encode()

    def decode(self):
        return self.__decode()

    def run(self):
        return self.__run()


if __name__ == "__main__":
    rot13 = Rot13()
    rot13.run()



# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ DOCUMENTATION ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #
# ROT13 - rotate by 13 is a simple encryption algorithm that replaces each letter in a string with the letter 13 positions away from it in the alphabet.
# It is a type of Caesar Cipher, which is a substitution cipher that replaces each letter in a message with a different letter a fixed number of positions down the alphabet