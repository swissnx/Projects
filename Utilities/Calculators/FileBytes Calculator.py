
import os


class FileBytesCalculator:
    def __init__(self):
        self.__file_name = input("File name: ")
        self.__unit = input("Unit (B, KB, MB, GB): ").upper()
        self.__validate_input()

    def __validate_input(self):
        if not os.path.isfile(self.__file_name):
            raise ValueError(f"{self.__file_name} is not a valid file name")

        if self.__unit not in ["B", "KB", "MB", "GB"]:
            raise ValueError(f"{self.__unit} is not a valid unit")

    def __calculate_file_size(self):
        try:
            file_size = os.path.getsize(self.__file_name)
            if self.__unit == "KB":
                file_size /= 1024
            elif self.__unit == "MB":
                file_size /= (1024 * 1024)
            elif self.__unit == "GB":
                file_size /= (1024 * 1024 * 1024)

            return file_size

        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def __calculate_line_sizes(self):
        try:
            with open(self.__file_name, "rb") as f:
                line_sizes = [len(line) for line in f]

                if self.__unit == "KB":
                    line_sizes = [size / 1024 for size in line_sizes]

                elif self.__unit == "MB":
                    line_sizes = [size / (1024 * 1024) for size in line_sizes]

                elif self.__unit == "GB":
                    line_sizes = [size / (1024 * 1024 * 1024) for size in line_sizes]

                return line_sizes

        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def __run(self):
        try:
            result = self.__calculate_file_size()
            print(f"The size of the file is: {result} {self.__unit}")

            line_sizes = self.__calculate_line_sizes()
            print("The size of each line in the file is:")

            for i, size in enumerate(line_sizes):
                print(f"Line {i + 1}: {size} {self.__unit}")

        except ValueError as ve:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{ve}\033[0m"

        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def run(self):
        self.__run()


if __name__ == "__main__":
    calculator = FileBytesCalculator()
    calculator.run()
