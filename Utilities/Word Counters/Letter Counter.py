
from os import strerror


class LetterCounter:
    def __init__(self, file_name):
        self.__counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
        self.__file_name = file_name

    def __count_letters(self):
        try:
            with open(self.__file_name, "rt") as f:
                for line in f:
                    for char in line:
                        if char.isalpha():
                            self.__counters[char.lower()] += 1
        except IOError as e:
            return f"\nI/O error occurred: {strerror(e.errno)}"

    def __output_counters(self):
        char_cnt = {}
        for char in self.__counters.keys():
            cnt = self.__counters[char]
            if cnt > 0:
                char_cnt.update({char: cnt})   # 2nd option: char_cnt[char] = cnt
        return char_cnt

    def run(self):
        try:
            error = self.__count_letters()

            if error:
                print(error)
            else:
                for char, cnt in self.__output_counters().items():
                    print(f"{char} -> {cnt}")

        except IOError as e:
            print(f"\nI/O error occurred: {strerror(e.errno)}")

        except Exception as e:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")


if __name__ == "__main__":
    file_name = input("File Path: ")
    letter_counter = LetterCounter(file_name)
    letter_counter.run()
