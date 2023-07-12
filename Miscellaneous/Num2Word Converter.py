
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

    def run(self):
        print("Enter a number in digits")
        while True:
            try:
                user_input = input("\nEnter: ")

                if user_input == "":
                    break
                
                user_num = int(user_input)
                print(self.__convert_num_to_word(user_num))

            except ValueError as e:
                return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"


if __name__ == "__main__":
    numconv = NumberConverter()
    numconv.run()



# write a code, input numbers from 1 to 100, output should be in words. For example, if input is 1 output should be one, and up to 100