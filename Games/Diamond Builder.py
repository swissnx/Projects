
class DiamondBuilder:
    def __init__(self):
        self.__n = int(input("Size: "))
        self.__symbol = input("Symbol: ")
        self.__filled = input("Fill the diamond? (y/n): ").lower() == "y"

    def __solve(self):
        result = []
        if self.__filled:
            for i in range(self.__n):
                row = []
                for j in range(self.__n - i - 1):
                    row.append(" ")
                for j in range(2 * i + 1):
                    row.append(self.__symbol)
                result.append("".join(row))
            for i in range(self.__n - 2, -1, -1):
                row = []
                for j in range(self.__n - i - 1):
                    row.append(" ")
                for j in range(2 * i + 1):
                    row.append(self.__symbol)
                result.append("".join(row))
        else:
            for i in range(self.__n):
                row = []
                for j in range(self.__n - i - 1):
                    row.append(" ")
                row.append(self.__symbol)
                if i != 0:
                    for j in range(2 * i - 1):
                        row.append(" ")
                    row.append(self.__symbol)
                result.append("".join(row))
            for i in range(self.__n - 2, -1, -1):
                row = []
                for j in range(self.__n - i - 1):
                    row.append(" ")
                row.append(self.__symbol)
                if i != 0:
                    for j in range(2 * i - 1):
                        row.append(" ")
                    row.append(self.__symbol)
                result.append("".join(row))
        return result

    def run(self):
        try:
            result = self.__solve()
            for row in result:
                print(row)
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")


if __name__ == "__main__":
    diamond = DiamondBuilder()
    diamond.run()
