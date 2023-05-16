
# This cipher was (probably) invented and used by Gaius Julius Caesar and his troops during the Gallic Wars. The idea is rather simple every letter of the message is replaced
# by its nearest consequent (A becomes B, B becomes C, and so on). The only exception is Z, which becomes A.
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
