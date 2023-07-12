
class PascalTriangle:
    def __init__(self):
        self.__num_rows = None
        self.__triangle = None

    def __generate_triangle(self):
        self.__triangle = []
        for row in range(self.__num_rows):
            new_row = [1]
            for col in range(1, row):
                new_row.append(self.__triangle[row - 1][col - 1] + self.__triangle[row - 1][col])
            if row:
                new_row.append(1)
            self.__triangle.append(new_row)

    def run(self):
        try:
            self.__num_rows = int(input("Number of Rows: "))

            if self.__num_rows < 0:
                raise Exception("Invalid number of rows")
            self.__generate_triangle()

            for row in self.__triangle:
                print(row)

        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")


if __name__ == "__main__":
    pt = PascalTriangle()
    pt.run()

# test cases: try to enter 5 or 7



# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ DOCUMENTATION ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #
# This program generates Pascal’s Triangle up to a specified number of rows. Pascal’s Triangle is a triangular array of numbers where each row is made up
# of the coefficients of the binomial expansion of (x + y) ^ n, where n is the row number. Each number in the triangle is the sum of the two numbers above it.

# The program takes input from the user for the number of rows to generate and then generates and prints Pascal’s Triangle up to that row.
# The program is implemented as a class with private attributes and methods. The run method can be called to run the program and take input from the user.

# This program can be useful for generating Pascal’s Triangle for mathematical or educational purposes.
# It is designed to be reusable and can be easily integrated into other programs.