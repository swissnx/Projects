
import codecs


class Rot13:
    def __init__(self):
        self.__message = None

    def __encode(self):
        try:
            return codecs.encode(self.__message, 'rot13')
        
        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def encode(self):
        return self.__encode()

    def __decode(self):
        try:
            return codecs.decode(self.__message, 'rot13')
        
        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def decode(self):
        return self.__decode()

    def __run(self):
        try:
            print("\nOptions:\n1. Encode\n2. Decode")
            prompt = input("\nChoice: ")

            if prompt.lower() == '1':
                self.__message = input("To Encode: ")
                encoded_message = self.__encode()
                print(f"\nEncoded message: {encoded_message}")

            elif prompt.lower() == '2':
                self.__message = input("To Decode: ")
                decoded_message = self.__decode()
                print(f"\nDecoded message: {decoded_message}")

            else:
                print("\nInvalid prompt. Please enter '1' or '2'")

        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def run(self):
        return self.__run()


if __name__ == "__main__":
    rot13 = Rot13()
    rot13.run()



# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ DOCUMENTATION ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #
# ROT13 - rotate by 13 is a simple encryption algorithm that replaces each letter in a string with the letter 13 positions away from it in the alphabet.
# It is a type of Caesar Cipher, which is a substitution cipher that replaces each letter in a message with a different letter a fixed number of positions down the alphabet