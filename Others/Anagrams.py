
class AnagramChecker:
    def __init__(self):
        self.__words = input('Enter words like (a, b): ').split(', ')

    def __are_anagrams(self):
        sorted_words = [sorted(word) for word in self.__words]
        return all(sorted_word == sorted_words[0] for sorted_word in sorted_words)

    def check(self):
        res = self.__are_anagrams()
        if res:
            print("Anagrams")
        else:
            print("Nope")


if __name__ == "__main__":
    checker = AnagramChecker()
    checker.check()
