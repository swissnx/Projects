
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

    @staticmethod
    def __encode(text):
        try:
            text = text.upper()
            encoded_text = ""
            for char in text:
                if char in MorseCode.__MORSE_CODES:
                    encoded_text += MorseCode.__MORSE_CODES[char] + ' '
                else:
                    encoded_text += char + ' '
            return encoded_text.strip()
        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    @staticmethod
    def encode(text):
        return MorseCode.__encode(text)

    @staticmethod
    def __decode(message):
        try:
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
        
        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    @staticmethod
    def decode(message):
        return MorseCode.__decode(message)

    def __run(self):
        try:
            while True:
                print("\n1. Encode --> Morse code\n2. Decode --> English\n3. Exit")
                prompt = int(input("\nChoice: "))

                if prompt not in [1, 2, 3]:
                    print("Invalid choice. Please try again.")
                    continue
                
                if prompt == 3:
                    break
                
                message = input("Message: ")

                if prompt == 1:
                    print(self.__encode(message))
                else:
                    print(self.__decode(message.strip()).capitalize())

        except ValueError:
            print("Invalid input. Please try again.")
            
        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def run(self):
        self.__run()


if __name__ == "__main__":
    morse_code = MorseCode()
    morse_code.run()
