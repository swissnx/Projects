
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

    def run(self):
        try:
            self.__sentence = input("Sentence: ")
            self.__check_pangram()
            
            if self.__is_pangram:
                print("It's a Pangram!")
            else:
                print("Not a pangram!")

        except Exception as e:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")


if __name__ == "__main__":
    p = Pangram()
    p.run()

# The quick brown fox jumps over the lazy dog
# Pack my box with five dozen liquor jugs



# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ FUNCTION ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #
# A pangram is a sentence that contains every letter of the alphabet at least once.

def pangram(sentence):
  char = [chr(i) for i in range(97, 96+27)]
  print(char)
  c = 0

  for i in range(len(sentence)):
    if sentence[i] in char and sentence[i] not in sentence[:i]:
      c += 1

  if c == 26:
    return True
  return False


user = input("> ")
print(pangram(user))
