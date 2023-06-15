
class MultiplicationTable:
    def __init__(self):
        self.__numbers = []
        self.__input_type = self.__get_input_type()
        if self.__input_type == 'range':
            self.__start = self.__get_positive_integer('\nFrom: ')
            self.__end = self.__get_positive_integer('Until: ')
            while self.__end <= self.__start:
                print("The end of the range must be greater than the start.")
                self.__end = self.__get_positive_integer('Until: ')
            for i in range(self.__start, self.__end+1):
                self.__numbers.append(i)
        elif self.__input_type == 'singular':
            self.__table_count = self.__get_positive_integer('\nHow many tables to generate?: ')
            for i in range(self.__table_count):
                self.__numbers.append(self.__get_positive_integer(f'Number {i+1}: '))
        if self.__input_type != 'exit':
            self.__format = input('\n1. Horizontal\n2. Vertical\n3. End\n\nChoice: ')
            while self.__format not in ['1', '2', '3']:
                print("Invalid input. Please enter 1, 2, or 3.")
                self.__format = input('\n1. Horizontal\n2. Vertical\n3. End\n\nChoice: ')
            if self.__format == '1':
                self.__format = 'horizontal'
            elif self.__format == '2':
                self.__format = 'vertical'
            else:
                return

    def __get_input_type(self):
        choice = input('\nOptions:\n1. Range\n2. Singular\n3. Exit\n\nChoice: ')
        while choice not in ['1', '2', '3']:
            print("Invalid input. Please enter 1, 2, or 3.")
            choice = input('\nOptions:\n1. Range\n2. Singular\n3. Exit\n\nChoice: ')
        if choice == '1':
            return 'range'
        elif choice == '2':
            return 'singular'
        else:
            return 'exit'

    def __get_positive_integer(self, prompt):
        while True:
            try:
                value = int(input(prompt))
                if value > 0:
                    return value
                else:
                    print("Please enter a positive integer.")
            except ValueError:
                print("Please enter a positive integer.")

    def __display_numbers(self):
        return f'The entered numbers are {", ".join(map(str, self.__numbers))}.\n'

    def __generate_multiplication_table(self):
        table = ""
        if self.__format == 'horizontal':
            for i in range(1, 11):
                row = ""
                for number in self.__numbers:
                    row += ('%d x %d = %d' %(number, i, number*i)).ljust(15)
                table += row + "\n"
        else:
            for number in self.__numbers:
                for i in range(1, 11):
                    table += ('%d x %d = %d' %(number, i, number*i)).ljust(15) + "\n"
                table += "\n"
        return table

    def __execute(self):
        try:
            print(self.__display_numbers())
            print(self.__generate_multiplication_table())
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

    def run(self):
        if self.__input_type != 'exit' and self.__format != '3':
            self.__execute()
            while True:
                choice = input("Try again? (y/n): ")
                if choice == 'y':
                    new_multiplication_table = MultiplicationTable()
                    new_multiplication_table.run()
                    break
                elif choice == 'n':
                    break
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")


if __name__ == "__main__":
    multiplication_table = MultiplicationTable()
    multiplication_table.run()
