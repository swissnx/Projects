
import time


class ASCIIConverter:
    @staticmethod
    def __to_ord(s: str, encoding: str) -> int:
        try:
            b = s.encode(encoding)
            if len(b) == 1:
                return b[0]
            else:
                raise ValueError(f'Invalid string length for {encoding} encoding')
        except Exception as e:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")
            return None

    @staticmethod
    def to_ord(s: str, encoding: str) -> int:
        return ASCIIConverter.__to_ord(s, encoding)

    @staticmethod
    def __to_chr(n: int, encoding: str) -> str:
        try:
            if (encoding == 'ascii' and n <= 0x7f) or (encoding == 'ISO-8859-1' and n <= 0xff):
                return bytes([n]).decode(encoding)
            else:
                raise ValueError(f'Invalid {encoding} character')
        except Exception as e:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")
            return None

    @staticmethod
    def to_chr(n: int, encoding: str) -> str:
        return ASCIIConverter.__to_chr(n, encoding)

    def __run(self):
        while True:
            try:
                print("\nOptions:\n1. ASCII-128\n2. ASCII-256\n3. Exit")
                choice = input("\nChoice: ")
                
                if choice == '1':
                    encoding = 'ascii'
                    max_value = 127
                elif choice == '2':
                    encoding = 'ISO-8859-1'
                    max_value = 255
                elif choice == "" or choice == '3':
                    break
                else:
                    continue

                print(f"\nOptions for {encoding}:\n1. String to {encoding}\n2. {encoding} to String\n3. List all {encoding} characters\n4. Save all {encoding} characters to file\n5. Back")
                choice = input("\nChoice: ")

                if choice == '1':
                    s = input("\nThe Character: ")
                    code_point = self.__to_ord(s, encoding)
                    if code_point is not None:
                        print(f"{encoding} #: {code_point}")

                elif choice == '2':
                    n = int(input(f"\n{encoding} #: "))
                    if n < 0 or n > max_value:
                        print(f"The entered value is not a valid {encoding} code point. Please enter a value between 0-{max_value}.")
                    else:
                        character = self.__to_chr(n, encoding)
                        if character is not None:
                            print(f"The Character: {character}")

                elif choice == '3':
                    for i in range(max_value + 1):
                        character = self.__to_chr(i, encoding)
                        if character is not None:
                            time.sleep(0.1)
                            print(f"{i}: {character}")

                elif choice == '4':
                    with open(f"{encoding}_characters.txt", "w", encoding="utf-8") as f:
                        for i in range(max_value + 1):
                            character = self.__to_chr(i, encoding)
                            if character is not None:
                                f.write(f"{i}: {character}\n")
                        print(f"All {encoding} characters have been saved to {encoding}_characters.txt")
            
            except Exception as e:
                return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def run(self):
        return self.__run()


if __name__ == "__main__":
    ascii_conv = ASCIIConverter()
    ascii_conv.run()
