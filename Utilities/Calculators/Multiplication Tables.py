
class MultiplicationTable:
    def __init__(self):
        self.__numbers = []
        self.__input_type = None
        self.__format = None

    def __get_input_type(self, choice):
        while choice not in ['1', '2', '0']:
            print("Invalid input. Please enter 1, 2, or 0.")
            choice = input('\nChoice: ')

        if choice == '1':
            return 'range'
        elif choice == '2':
            return 'singular'
        else:
            return 'exit'

    def __get_range(self):
        start = self.__get_positive_integer('\nFrom: ')
        end = self.__get_positive_integer('Until: ')

        while end <= start:
            print("The end of the range must be greater than the start.")
            end = self.__get_positive_integer('Until: ')

        for i in range(start, end + 1):
            self.__numbers.append(i)

    def __get_singular_numbers(self):
        table_count = self.__get_positive_integer('\nHow many tables to generate?: ')

        for i in range(table_count):
            self.__numbers.append(self.__get_positive_integer(f'Number {i + 1}: '))

    def __get_format(self):
        format_choice = input('\n1. Horizontal\n2. Vertical\n0. End\n\nChoice: ')

        while format_choice not in ['1', '2', '0']:
            print("Invalid input. Please enter 1, 2, or 0.")
            format_choice = input('\nChoice: ')

        if format_choice == '1':
            return 'horizontal'
        elif format_choice == '2':
            return 'vertical'
        elif format_choice == '0':
            return

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
        return ", ".join(map(str, self.__numbers))

    def __generate_multiplication_table(self):
        table = ""
        if self.__format == 'horizontal':
            for i in range(1, 11):
                row = ""
                for number in self.__numbers:
                    row += ('%d x %d = %d' % (number, i, number * i)).ljust(15)
                table += row + "\n"
        else:
            for number in self.__numbers:
                for i in range(1, 11):
                    table += ('%d x %d = %d' % (number, i, number * i)).ljust(15) + "\n"
                table += "\n"
        return table

    def run(self):
        choice = input('\n1. Range\n2. Singular\n0. Exit\n\nChoice: ')
        self.__input_type = self.__get_input_type(choice)

        if self.__input_type == 'range':
            self.__get_range()
        elif self.__input_type == 'singular':
            self.__get_singular_numbers()

        if self.__input_type != 'exit':
            self.__format = self.__get_format()

            if self.__format != None:
                print(f'The entered numbers are {self.__display_numbers()}.\n')
                print(self.__generate_multiplication_table())

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
