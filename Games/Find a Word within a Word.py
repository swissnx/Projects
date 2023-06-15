
class WordFinder:
    def __init__(self):
        self.__word = input("Word to find: ").upper()
        self.__string = input("String to search through: ").upper()
        self.__found = True
        self.__start = 0

    def __find_word(self):
        for ch in self.__word:
            pos = self.__string.find(ch, self.__start)
            if pos < 0:
                self.__found = False
                break
            self.__start = pos + 1

    def __run(self):
        if not self.__word or not self.__string:
            print("Exiting program: word or string to search through cannot be empty.")
            return
        self.__find_word()
        if self.__found:
            print("Yes")
        else:
            print("No")

    def run(self):
        try:
            return self.__run()
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

if __name__ == "__main__":
    word_finder = WordFinder()
    word_finder.run()
