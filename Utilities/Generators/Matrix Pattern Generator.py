
class MatrixPatternGenerator:
    def __init__(self):
        self.__pattern = None

    def __generate_pattern(self, rows, columns):
        self.__pattern = [[0 for j in range(columns)] for i in range(rows)]

    def __fill_function(self, i, j):
        return (i + 1) * (j + 1)#0

    def fill_matrix(self):
        for i in range(len(self.__pattern)):
            for j in range(len(self.__pattern[0])):
                self.__pattern[i][j] = self.__fill_function(i, j)

    def __run(self):
        rows = int(input("Number of rows: "))
        columns = int(input("Number of columns: "))
        self.__generate_pattern(rows, columns)
        self.fill_matrix()
        for row in self.__pattern:
            print(row)

    def run(self):
        try:
            self.__run()
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")


if __name__ == "__main__":
    matrix_gen = MatrixPatternGenerator()
    matrix_gen.run()
