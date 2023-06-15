
class Pangram:
    def __init__(self):
        self.__sentence = None
        self.__is_pangram = None

    def __check_pangram(self):
        alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        for char in alphabet:
            if char not in self.__sentence.lower():
                self.__is_pangram = False
                return
        self.__is_pangram = True

    def __run(self):
        try:
            self.__sentence = input("Sentence: ")
            self.__check_pangram()
            if self.__is_pangram:
                print("It is a pangram!")
            else:
                print("Not a pangram!")
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

    def run(self):
        return self.__run()


if __name__ == "__main__":
    p = Pangram()
    p.run()

# The quick brown fox jumps over the lazy dog
# Pack my box with five dozen liquor jugs



# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ FUNCTION ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #
# A pangram is a sentence that contains every letter of the alphabet at least once.
