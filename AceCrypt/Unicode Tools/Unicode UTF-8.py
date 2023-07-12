
import time


class UnicodeConverter:
    @staticmethod
    def __to_ord(s: str) -> int:
        # converts a string to its corresponding unicode char using UTF-8 encoding
        try:
            b = s.encode('utf-8')
            if len(b) == 1:
                return b[0]
            elif len(b) == 2:
                return ((b[0] & 0x1f) << 6) | (b[1] & 0x3f)
            elif len(b) == 3:
                return ((b[0] & 0x0f) << 12) | ((b[1] & 0x3f) << 6) | (b[2] & 0x3f)
            elif len(b) == 4:
                return ((b[0] & 0x07) << 18) | ((b[1] & 0x3f) << 12) | ((b[2] & 0x3f) << 6) | (b[3] & 0x3f)
            else:
                raise ValueError('Invalid string length for UTF-8 encoding')
            
        except Exception as e:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")
            return None

    @staticmethod
    def to_ord(s: str) -> int:
        return UnicodeConverter.__to_ord(s)

    @staticmethod
    def __to_chr(n: int) -> str:
        # converts a unicode code to its corresponding character using UTF-8 encoding
        try:
            if n <= 0x7f:
                return chr(n)
            elif n <= 0x7ff:
                return chr(0xc0 | (n >> 6)) + chr(0x80 | (n & 0x3f))
            elif n <= 0xffff:
                return chr(0xe0 | (n >> 12)) + chr(0x80 | ((n >> 6) & 0x3f)) + chr(0x80 | (n & 0x3f))
            elif n <= 0x10ffff:
                return chr(0xf0 | (n >> 18)) + chr(0x80 | ((n >> 12) & 0x3f)) + chr(0x80 | ((n >> 6) & 0x3f)) + chr(0x80 | (n & 0x3f))
            else:
                raise ValueError('Invalid Unicode character')
            
        except Exception as e:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")
            return None

    @staticmethod
    def to_chr(n: int) -> str:
        return UnicodeConverter.__to_chr(n)

    def __run(self):
        while True:
            try:
                print("\nOptions:\n1. String to Unicode\n2. Unicode to String\n3. List all UTF-8 characters\n4. Save all UTF-8 characters to file\n0. Exit")
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
                    with open("utf8_characters.txt", "w", encoding="utf-8") as f:
                        for i in range(1114112):
                            character = self.__to_chr(i)
                            if character is not None:
                                f.write(f"{i}: {character}\n")
                    print("All UTF-8 characters have been saved to utf8_characters.txt")

                elif choice == '0' or choice == "":
                    break
                
            except Exception as e:
                return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def run(self):
        return self.__run()


if __name__ == "__main__":
    unicode = UnicodeConverter()
    unicode.run()
