
class AcronymGenerator:
    def __init__(self):
        self.__phrase = None
        self.__acronym = None

    def __generate_acronym(self):
        words = self.__phrase.split()
        self.__acronym = ''.join(word[0].upper() for word in words)

    def generate_acronym(self, phrase):
        self.__phrase = phrase
        self.__generate_acronym()
        return self.__acronym

    def __run(self):
        while True:
            try:
                self.__phrase = input('Phrase: ')
                if not all(c.isalpha() or c.isspace() for c in self.__phrase):
                    raise ValueError
                break
            except ValueError:
                print('Please enter a valid phrase - letters and spaces only.')
        self.__generate_acronym()
        print(f'Acronym: {self.__acronym}')

    def run(self):
        return self.__run()


if __name__ == "__main__":
    action = AcronymGenerator()
    action.run()