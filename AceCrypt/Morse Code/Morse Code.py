
class MorseCode:
    __MORSE_CODES = {'A': '.-',
                    'B': '-...',
                    'C': '-.-.',
                    'D': '-..',
                    'E': '.',
                    'F': '..-.',
                    'G': '--.',
                    'H': '....',
                    'I': '..',
                    'J': '.---',
                    'K': '-.-',
                    'L': '.-..',
                    'M': '--',
                    'N': '-.',
                    'O': '---',
                    'P': '.--.',
                    'Q': '--.-',
                    'R': '.-.',
                    'S': '...',
                    'T': '-',
                    'U': '..-',
                    'V': '...-',
                    'W': '.--',
                    'X': '-..-',
                    'Y': '-.--',
                    'Z': '--..',
                    '0': '-----',
                    '1': '.----',
                    '2': '..---',
                    '3': '...--',
                    '4': '....-',
                    '5': '.....',
                    '6': '-....',
                    '7': '--...',
                    '8': '---..',
                    '9': '----.',
                    ' ': '_',
                    '?': '..--..',
                    '!': '-.-.--',
                    '.': '.-.-.-',
                    ',': '--..--',
                    ';': '-.-.-.',
                    ':': '---...',
                    '+': '.-.-.',
                    '-': '-....-',
                    '/': '-..-.',
                    '=': '-...-'
}

    def __run(self):
        while True:
            print("\n1. Encode --> Morse code")
            print("2. Decode --> English")
            print("3. Exit")
            try:
                prompt = int(input("\nChoice: "))
                if prompt not in [1, 2, 3]:
                    print("Invalid choice. Please try again.")
                    continue
                if prompt == 3:
                    break
                message = input("Enter the message: ")
                if prompt == 1:
                    print(self.__encode(message))
                else:
                    print(self.__decode(message.strip()).capitalize())
            except ValueError:
                print("Invalid input. Please try again.")

    @staticmethod
    def __encode(text):
        text = text.upper()
        encoded_text = ""
        for char in text:
            if char in MorseCode.__MORSE_CODES:
                encoded_text += MorseCode.__MORSE_CODES[char] + ' '
            else:
                encoded_text += char + ' '
        return encoded_text.strip()

    @staticmethod
    def encode(text):
        return MorseCode.__encode(text)

    @staticmethod
    def __decode(message):
        decoded_message = ""
        morse_code_list = message.split(' ')
        for code in morse_code_list:
            if code == '_':
                decoded_message += ' '
            elif code in MorseCode.__MORSE_CODES.values():
                decoded_message += list(MorseCode.__MORSE_CODES.keys())[list(MorseCode.__MORSE_CODES.values()).index(code)]
            else:
                decoded_message += code
        return decoded_message

    @staticmethod
    def decode(message):
        return MorseCode.__decode(message)

    def run(self):
        self.__run()


if __name__ == "__main__":
    morse_code = MorseCode()
    morse_code.run()
