
class NumberPrinter:
    def __init__(self):
        self.__digits = ['1111110',
                         '0110000',
                         '1101101',
                         '1111001',
                         '0110011',
                         '1011011',
                         '1011111',
                         '1110000',
                         '1111111',
                         '1111011']
        self.__num = input("Display Number: ")
        self.__width = int(input("Width (def-7): ") or 7)
        self.__height = int(input("Height (default-5): ") or 5)
        self.__space = int(input("Space between numbers (default-1): ") or 1)
        self.__symbol = input("Enter the symbol to use for display (default is #): ") or '#'
        self.__color = input("Color (red, green, yellow, blue, magenta, cyan, white): ")

    def __print_number(self):
        num = self.__num
        digs = str(num)
        lines = ["" for _ in range(self.__height)]
        for d in digs:
            segs = [[" " for _ in range(self.__width)] for _ in range(self.__height)]
            ptrn = self.__digits[ord(d) - ord('0')]
            if ptrn[0] == '1':
                for i in range(self.__width):
                    segs[0][i] = self.__symbol
            if ptrn[1] == '1':
                for i in range(self.__height // 2):
                    segs[i][self.__width - 1] = self.__symbol
            if ptrn[2] == '1':
                for i in range(self.__height // 2, self.__height):
                    segs[i][self.__width - 1] = self.__symbol
            if ptrn[3] == '1':
                for i in range(self.__width):
                    segs[self.__height - 1][i] = self.__symbol
            if ptrn[4] == '1':
                for i in range(self.__height // 2, self.__height):
                    segs[i][0] = self.__symbol
            if ptrn[5] == '1':
                for i in range(self.__height // 2):
                    segs[i][0] = self.__symbol
            if ptrn[6] == '1':
                for i in range(self.__width):
                    segs[self.__height // 2][i] = self.__symbol
            for lin in range(self.__height):
                lines[lin] += ''.join(segs[lin]) + " " * self.__space
        return lines

    def __run(self):
        try:
            num = int(self.__num)
            lines = self. __print_number()
            colors = {
                "red": "\033[31m",
                "green": "\033[32m",
                "yellow": "\033[33m",
                "blue": "\033[34m",
                "magenta": "\033[35m",
                "cyan": "\033[36m",
                "white": "\033[37m"
            }
            color_code = colors.get(self.__color.lower(), "\033[37m")
            reset_code = "\033[0m"
            for line in lines:
                print(color_code + line + reset_code)
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

    def run(self):
        return self. __run()


if __name__ == "__main__":
    printer = NumberPrinter()
    printer.run()
