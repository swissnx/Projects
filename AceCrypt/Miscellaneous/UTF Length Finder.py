
class UTFLengthFinder:
    def __init__(self):
        pass

    @staticmethod
    def __len_encoding(message):
        try:
            if message == "":
                raise ValueError("Message cannot be empty")

            try:
                utf_8 = len(message.encode('utf-8'))
            except UnicodeDecodeError:
                utf_8 = None

            try:
                utf_16 = len(message.encode('utf-16'))
            except UnicodeDecodeError:
                utf_16 = None

            try:
                utf_32 = len(message.encode('utf-32'))
            except UnicodeDecodeError:
                utf_32 = None

            return utf_8, utf_16, utf_32

        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    @staticmethod
    def len_encoding(message):
        return UTFLengthFinder.__len_encoding(message)

    def run(self):
        try:
            while True:
                print("\nCalculate length:\n1. Text\n2. Code\n0. Exit")
                argument = input("\nChoice: ")

                if argument == "0" or argument == "":
                    break

                elif argument == "1":
                    text = input("\nMessage: ")
                    utf_8, utf_16, utf_32 = self.len_encoding(text)

                    if utf_8 is not None:
                        print(f"\nUTF-8 : {str(utf_8)} bytes")

                    if utf_16 is not None:
                        print(f"UTF-16: {str(utf_16)} bytes")

                    if utf_32 is not None:
                        print(f"UTF-32: {str(utf_32)} bytes")


                elif argument == "2":
                    print("\nEnter/Paste code below ('abschluss' to finish)")

                    lines = []

                    while True:
                        line = input("\nInput: ")

                        if line == "abschluss" and (not lines or not lines[-1]):
                            break
                        
                        lines.append(line)

                    code = "\n".join(lines)

                    utf_8, utf_16, utf_32 = self.len_encoding(code)

                    if utf_8 is not None:
                        print(f"\nUTF-8 : {str(utf_8)} bytes")

                    if utf_16 is not None:
                        print(f"UTF-16: {str(utf_16)} bytes")

                    if utf_32 is not None:
                        print(f"UTF-32: {str(utf_32)} bytes")

        except ValueError as ve:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{ve}\033[0m"
        
        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"


if __name__ == "__main__":
    utf_len = UTFLengthFinder()
    utf_len.run()