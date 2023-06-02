
# This cipher was (probably) invented and used by Gaius Julius Caesar and his troops during the Gallic Wars. The idea is rather simple every letter
# of the message is replaced by its nearest consequent (A becomes B, B becomes C, and so on). The only exception is Z, which becomes A.
# We've written it using the following assumptions:
#  • it accepts Latin letters only (note: the Romans used neither whitespaces nor digits)
#  • all letters of the message are in upper case (note: the Romans knew only capitals)

class CaesarsCipher:
    def __init__(self):
        pass

    def encrypt(self):
        text = input("Enter your message: ")   # ask the user to enter the open (unencrypted), one-line message;
        cipher = ''                            # prepare a string for an encrypted message (empty for now)
        for char in text:                      # start the iteration through the message;
            if not char.isalpha():             # if the current character is not alphabetic...
                continue                       # ...ignore it;
            char = char.upper()                # convert the letter to upper-case (it's preferable to do it blindly, rather than checking whether it's needed or not)
            code = ord(char) + 1               # get the code of the letter and increment it by one;
            if code > ord('Z'):                # if the resulting code has "left" the Latin alphabet (if it's greater than the Z code)...
                code = ord('A')                # ...change it to the A code;
            cipher += chr(code)                # append the received character to the end of the encrypted message;
        
        print(cipher)

    def decrypt(self):
        cipher = input('Enter your cryptogram: ')
        text = ''
        for char in cipher:
            if not char.isalpha():
                continue
            char = char.upper()
            code = ord(char) - 1
            if code < ord('A'):
                code = ord('Z')
            text += chr(code)

        print(text)


if __name__ == "__main__":
    julius = CaesarsCipher()
    julius.encrypt()
    julius.decrypt()



""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# ================================ CAESAR'S CIPHER (ADVANCED) ================================

# Test 1: Encryption : works only for lowercase
import string

plain_text = "hello world"
shift = 5                             # w/o (%26) any input number must be between 1 and 26

alphabet = string.ascii_lowercase
shifted = alphabet[shift:] + alphabet[:shift]
table = str.maketrans(alphabet, shifted)

encrypted = plain_text.translate(table)

print(encrypted)


# Test 2: Encryption : works only for lowercase
import string

plain_text = "hello world"
shift = 80
shift %= 26    # cause the limit of the alphabet is 26 and any number input there is divisible by 26 creating a loop within 26

alphabet = string.ascii_lowercase
shifted = alphabet[shift:] + alphabet[:shift]
table = str.maketrans(alphabet, shifted)

encrypted = plain_text.translate(table)

print(encrypted)

#+++++++++++++++++++++++++++++++++++++

# Test 1: Decryption : works only for lowercase
import string

plain_text = "jgnnq yqtnf"
shift = 26 - 80      # hello world
shift %= 26    # cause the limit of the alphabet is 26 and any number input there is divisible by 26 creating a loop within 26

alphabet = string.ascii_lowercase
shifted = alphabet[shift:] + alphabet[:shift]
table = str.maketrans(alphabet, shifted)

encrypted = plain_text.translate(table)

print(encrypted)


#+++++++++++++++++++++++++++++++++++++

# Finalized: Encryption
import string

def caesar(text, shift, characters):

    def shift_abc(alphabet):
        return alphabet[shift:] + alphabet[:shift]

    shifted_abc = tuple(map(shift_abc, characters))
    final_alphabet = "".join(characters)
    final_shifted_abc = "".join(shifted_abc)
    table = str.maketrans(final_alphabet, final_shifted_abc)
    return text.translate(table)

message = input("\nEnter a message: ")
shift_num = shift(int(input("Enter a number: ")))
print(caesar(message, shift_num, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]))


#+++++++++++++++++++++++++++++++++++++

# Finalized - option 1:
text = input("Enter message: ")        # input text to encrypt

shift = 0           # enter valid shift value (repeat until it succeeds)

while shift == 0:
    try:
        shift = int(input("Enter cipher's shift (1..25): "))
        if shift not in range(1,26):
            raise ValueError
    except ValueError:
        shift = 0
    if shift == 0:
        print("Bad shift value!")

cipher = ""

for char in text:
    if char.isalpha():             # is it a letter?
        code = ord(char) + shift   # shift its code
        if char.isupper():         # find the code of the first letter (upper- or lower-case)
            first = ord('A')
        else:
            first = ord('a')
        code -= first          # make correction
        code %= 26
        cipher += chr(first + code)    # append encoded character to message
    else:
        cipher += char         # append original character to message

print(cipher)


#+++++++++++++++++++++++++++++++++++++

# Finalized - option 2: with 2 sample tests
text = input("Enter message: ")        # input: A           |   input: c

shift = int(input("Enter a number: "))  # input: 2          |   input: 3
shift %= 26

cipher = ""

for char in text:
    if char.isalpha():
        code = ord(char) + shift    # A = 65 -->>    67 = 65 + 2       |   # c = 99 -->> 99+3 = 102
        if char.isupper():
            first = ord('A')     # first = 65
        else:
            first = ord('a')     # first = 97
        code -= first         # 67 - 65 = 2                         |    # 102 - 97 = 5
        code %= 26            # 2 % 26 = 2                          |    # 5 % 26 = 5
        cipher += chr(first + code)    # 65 + 2 = chr(67) = C       |    # 97+5 = chr(102) = f
    else:
        cipher += char

print(cipher)
