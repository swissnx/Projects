
import time


class ASCII128:
    @staticmethod
    def __to_ord(s: str) -> int:
        # converts a string to its corresponding ASCII code
        try:
            b = s.encode('ascii')
            if len(b) == 1:
                return b[0]
            else:
                raise ValueError('Invalid string length for ASCII encoding')
        except Exception as e:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")
            return None

    @staticmethod
    def to_ord(s: str) -> int:
        return ASCII128.__to_ord(s)

    @staticmethod
    def __to_chr(n: int) -> str:
        # converts an ASCII code to its corresponding character
        try:
            if n <= 0x7f:
                return chr(n)
            else:
                raise ValueError('Invalid ASCII character')
        except Exception as e:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")
            return None

    @staticmethod
    def to_chr(n: int) -> str:
        return ASCII128.__to_chr(n)

    def __run(self):
        while True:
            try:
                print("\nOptions:\n1. String to ASCII\n2. ASCII to String\n3. List all ASCII characters\n4. Save all ASCII characters to file\n0. Exit")
                choice = input("\nChoice: ")

                if choice == '1':
                    s = input("\nThe Character: ")
                    code_point = self.__to_ord(s)
                    if code_point is not None:
                        print(f"ASCII #: {code_point}")

                elif choice == '2':
                    n = int(input("\nASCII #: "))
                    if n < 0 or n > 127:
                        print("The entered value is not a valid ASCII code point. Please enter a value between 0-127.")
                    else:
                        character = self.__to_chr(n)
                        if character is not None:
                            print(f"The Character: {character}")

                elif choice == '3':
                    for i in range(128):
                        character = self.__to_chr(i)
                        if character is not None:
                            time.sleep(0.1)
                            print(f"{i}: {character}")

                elif choice == '4':
                    with open("ascii_characters.txt", "w", encoding="utf-8") as f:
                        for i in range(128):
                            character = self.__to_chr(i)
                            if character is not None:
                                f.write(f"{i}: {character}\n")

                    print("All ASCII characters have been saved to ascii_characters.txt")
                elif choice == "" or choice == '0':
                    break
                
            except Exception as e:
                return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def run(self):
        return self.__run()


if __name__ == "__main__":
    ascii_128 = ASCII128()
    ascii_128.run()
