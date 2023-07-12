
class RomanNumerals:
    def __init__(self):
        self.__roman_map = {1: "I",
                            4: "IV",
                            5: "V",
                            9: "IX",
                            10: "X",
                            40: "XL",
                            50: "L",
                            90: "XC",
                            100: "C",
                            400: "CD",
                            500: "D",
                            900: "CM",
                            1000: "M"}

    def __to_roman(self, n: int) -> str:
        try:
            if not 0 < n < 4000:
                raise ValueError(f"Invalid input: {n}. Input must be between 1-3999.")
            
            result = ''
            for num, r in sorted(self.__roman_map.items(), reverse=True):
                while n >= num:
                    result += r
                    n -= num
            return result
        
        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def to_roman(self, n: int) -> str:
        return self.__to_roman(n)

    def __from_roman(self, roman: str) -> int:
        try:
            result = 0
            index = 0

            for num, r in sorted(self.__roman_map.items(), key=lambda x: len(x[1]), reverse=True):
                while roman[index:index+len(r)] == r:
                    result += num
                    index += len(r)

            if index != len(roman):
                raise ValueError(f"Invalid Roman numeral: {roman}")
            
            return result
        
        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def from_roman(self, roman: str) -> int:
        return self.__from_roman(roman)

    def __run(self):
        try:
            while True:
                action = input("\nEnter: ")
                
                if action == '0' or action == "":
                    break
                
                try:
                    numeral = int(action)
                    print(f"{numeral} --> {self.__to_roman(numeral)}")

                except ValueError:
                    try:
                        print(f"{action} --> {self.__from_roman(action)}")

                    except ValueError:
                        print(f"Invalid input: {action}")

        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def run(self):
        return self.__run()


if __name__ == "__main__":
    roman_numerals = RomanNumerals()
    roman_numerals.run()
