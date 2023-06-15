
class NumberConverter:
    def __init__(self):
        self.__ones_place = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        self.__tens_place = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
        self.__special_nums = {11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
                               16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

    def __convert_num_to_word(self, num):
        if num == 0:
            return 'zero'
        if num < 10:
            return self.__ones_place[num - 1]
        elif num < 20:
            return self.__special_nums[num]
        elif num < 100:
            tens_digit = num // 10
            ones_digit = num % 10
            if ones_digit == 0:
                return self.__tens_place[tens_digit - 1]
            else:
                return self.__tens_place[tens_digit - 1] + ' ' + self.__ones_place[ones_digit - 1]
        else:
            return f'Invalid input: {num}'

    def __run(self):
        print("Enter a number in digits (or press enter to quit)")
        while True:
            try:
                user_input = input("\nEnter: ")
                if user_input == "":
                    break
                user_num = int(user_input)
                print(self.__convert_num_to_word(user_num))
            except ValueError as e:
                print(f"\n\u001b[3m** An error occurred: \u001b[38;5;196m{e}\u001b[0m")
                break

    def run(self):
        self.__run()


if __name__ == "__main__":
    numconv = NumberConverter()
    numconv.run()
