
import time


class UnicodeConverterUTF32:
    @staticmethod
    def __to_ord(s: str) -> int:
        # converts a string to its corresponding unicode char using UTF-32 encoding
        try:
            b = s.encode('utf-32')
            if len(b) == 4:
                return int.from_bytes(b, byteorder='little')
            else:
                raise ValueError('Invalid string length for UTF-32 encoding')
            
        except Exception as e:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")
            return None

    @staticmethod
    def to_ord(s: str) -> int:
        return UnicodeConverterUTF32.__to_ord(s)

    @staticmethod
    def __to_chr(n: int) -> str:
        # converts a unicode code to its corresponding character using UTF-32 encoding
        try:
            if n <= 0x10ffff:
                return chr(n)
            else:
                raise ValueError('Invalid Unicode character')
            
        except Exception as e:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")
            return None

    @staticmethod
    def to_chr(n: int) -> str:
        return UnicodeConverterUTF32.__to_chr(n)

    def __run(self):
        while True:
            try:
                print("\nOptions:\n1. String to Unicode\n2. Unicode to String\n3. List all UTF-32 characters\n4. Save all UTF-32 characters to file\n0. Exit")
                choice = input("\nChoice: ")

                if choice == '1':
                    s = input("\nThe Character: ")
                    code_point = self.__to_ord(s)
                    if code_point is not None:
                        print(f"Unicode #: {code_point}")

                elif choice == '2':
                    n = int(input("\nUnicode #: "))
                    if n < 0 or n > 1114111:
                        print("The entered value is not a valid Unicode code point. Please enter a value between 0-1114111.")
                    else:
                        character = self.__to_chr(n)
                        if character is not None:
                            print(f"The Character: {character}")

                elif choice == '3':
                    for i in range(1114112):
                        character = self.__to_chr(i)
                        if character is not None:
                            time.sleep(0.1)
                            print(f"{i}: {character}")

                elif choice == '4':
                    with open("utf32_characters.txt", "w", encoding="utf-8") as f:
                        for i in range(1114112):
                            character = self.__to_chr(i)
                            if character is not None:
                                f.write(f"{i}: {character}\n")
                    print("All UTF-32 characters have been saved to utf32_characters.txt")

                elif choice == '0' or choice == "":
                    break
                
            except Exception as e:
                return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def run(self):
        return self.__run()


if __name__ == "__main__":
    unicode = UnicodeConverterUTF32()
    unicode.run()
