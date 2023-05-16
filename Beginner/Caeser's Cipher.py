
class CaesarCipher:
    def __init__(self, shift_num):
        self.shift_num = shift_num

    def encrypt(self, message):
        def shift(char):
            offset = 65 if char.isupper() else 97
            return chr((ord(char) + self.shift_num - offset) % 26 + offset)
        return ''.join([shift(char) for char in message])

    def decrypt(self, cryptogram):
        def shift(char):
            offset = 65 if char.isupper() else 97
            return chr((ord(char) + 26 - self.shift_num - offset) % 26 + offset)
        return ''.join([shift(char) for char in cryptogram])


while True:
    print("\nOptions:\n1. Encode Text\n2. Decode Text\n3. Exit")
    action = input("\nYour choice: ").upper()
    if action.upper() == '3' or action == "":
        break
    elif action not in ['1', '2']:
        print("Invalid input. Please enter 1, 2, or 3.")
        continue

    message = input("Enter message: ")
    while True:
        try:
            shift_num = int(input("Shift number between 1-25: "))
            if shift_num < 1 or shift_num > 25:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a number between 1-25.")

    cipher = CaesarCipher(shift_num)

    if action == "1":
        print(f"Ciphered Text: {cipher.encrypt(message)}")
    elif action == "2":
        print(f"Decrypted Text: {cipher.decrypt(message)}")
    else:
        print("Wrong input. It is 1 for encoding, 2 for decoding.")
