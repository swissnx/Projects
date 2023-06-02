
class CaesarCipher:
    def __init__(self):
        self.__shift_num = None

    def __encrypt(self, message):
        def shift(char):
            offset = 65 if char.isupper() else 97
            return chr((ord(char) + self.__shift_num - offset) % 26 + offset)
        return ''.join([shift(char) for char in message])

    def __decrypt(self, cryptogram):
        def shift(char):
            offset = 65 if char.isupper() else 97
            return chr((ord(char) + 26 - self.__shift_num - offset) % 26 + offset)
        return ''.join([shift(char) for char in cryptogram])

    def __run(self):
        while True:
            print("\nOptions:\n1. Encode Text\n2. Decode Text\n3. Exit")
            action = input("\nYour choice: ").upper()
            if action == '3' or action == "":
                break
            elif action not in ['1', '2']:
                print("Invalid input. Please enter 1, 2, or 3.")
                continue

            message = input("Message: ")
            while True:
                try:
                    self.__shift_num = int(input("Shift number between 1-25: "))
                    if self.__shift_num < 1 or self.__shift_num > 25:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid input. Please enter a number between 1-25.")

            if action == "1":
                print(f"Ciphered Text: {self.__encrypt(message)}")
            elif action == "2":
                print(f"Decrypted Text: {self.__decrypt(message)}")
            else:
                print("Wrong input. It is 1 for encoding, 2 for decoding.")

    def encrypt(self, message):
        return self.__encrypt(message)
    
    def decrypt(self, cryptogram):
        return self.__decrypt(cryptogram)

    def run(self):
        return self.__run()


if __name__ == "__main__":
    cipher = CaesarCipher()
    cipher.run()
