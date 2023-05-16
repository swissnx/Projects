import codecs


class Rot13:
    def __init__(self):
        self.message = ''

    def encode(self):
        self.message = input("To Encode: ")
        try:
            return codecs.encode(self.message, 'rot13')
        except Exception as e:
            print(f"An error: {e}")

    def decode(self):
        self.message = input("To Decode: ")
        try:
            return codecs.decode(self.message, 'rot13')
        except Exception as e:
            print(f"An error: {e}")


rot13 = Rot13()
prompt = input("Would you like to encode or decode a message? (1. encode/2. decode): ")

if prompt.lower() == '1':
    encoded_message = rot13.encode()
    print(f"Encoded message: {encoded_message}")
elif prompt.lower() == '2':
    decoded_message = rot13.decode()
    print(f"Decoded message: {decoded_message}")
else:
    print("Invalid prompt. Please enter '1' or '2'")
