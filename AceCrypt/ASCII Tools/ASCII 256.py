
import time


class ASCII256:
    @staticmethod
    def __to_ord(s: str) -> int:
        # converts a string to its corresponding ISO-8859-1 code
        try:
            b = s.encode('ISO-8859-1')
            if len(b) == 1:
                return b[0]
            else:
                raise ValueError('Invalid string length for ISO-8859-1 encoding')
        except Exception as e:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")
            return None

    @staticmethod
    def to_ord(s: str) -> int:
        return ISO88591Converter.__to_ord(s)

    @staticmethod
    def __to_chr(n: int) -> str:
        # converts an ISO-8859-1 code to its corresponding character
        try:
            if n <= 0xff:
                return bytes([n]).decode('ISO-8859-1')
            else:
                raise ValueError('Invalid ISO-8859-1 character')
        except Exception as e:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")
            return None

    @staticmethod
    def to_chr(n: int) -> str:
        return ISO88591Converter.__to_chr(n)

    def __run(self):
        while True:
            try:
                print("\nOptions:\n1. String to ISO-8859-1\n2. ISO-8859-1 to String\n3. List all ISO-8859-1 characters\n4. Save all ISO-8859-1 characters to file\n5. Exit")
                choice = input("\nChoice: ")

                if choice == '1':
                    s = input("\nThe Character: ")
                    code_point = self.__to_ord(s)
                    if code_point is not None:
                        print(f"ISO-8859-1 #: {code_point}")

                elif choice == '2':
                    n = int(input("\nISO-8859-1 #: "))
                    if n < 0 or n > 255:
                        print("The entered value is not a valid ISO-8859-1 code point. Please enter a value between 0-255.")
                    else:
                        character = self.__to_chr(n)
                        if character is not None:
                            print(f"The Character: {character}")

                elif choice == '3':
                    for i in range(256):
                        character = self.__to_chr(i)
                        if character is not None:
                            time.sleep(0.1)
                            print(f"{i}: {character}")

                elif choice == '4':
                    with open("iso_8859_1_characters.txt", "w", encoding="utf-8") as f:
                        for i in range(256):
                            character = self.__to_chr(i)
                            if character is not None:
                                f.write(f"{i}: {character}\n")

                    print("All ISO-8859-1 characters have been saved to iso_8859_1_characters.txt")

                elif choice == "" or choice == '5':
                    break

            except Exception as e:
                return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def run(self):
        return self.__run()


if __name__ == "__main__":
    ascii_256 = ASCII256()
    ascii_256.run()
