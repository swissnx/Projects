
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




#●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ DOCUMENTATION ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #
# This program defines an AnagramChecker class that checks if a given set of words are anagrams of each other.
# Test cases: heart, earth

# Sample_1
def anagram(*words):
  return sorted(words)

res = anagram('heart', 'earth')
x = sorted(res[0])  # x = sorted(list(res[0]))
y = sorted(res[1])  # y = sorted(list(res[1]))

if x == y:
  print("anagrams")
else:
  print("nope")



# Sample_2
str_1 = input("Enter the first string: ")
str_2 = input("Enter the second string: ")

strx_1 = ''.join(sorted(list(str_1.upper().replace(' ',''))))
strx_2 = ''.join(sorted(list(str_2.upper().replace(' ',''))))
if len(strx_1) > 0 and strx_1 == strx_2:
	print("Anagrams")
else:
	print("Not anagrams")



# Sample_3
str_1 = input("Enter the first string: ").upper()
str_2 = input("Enter the second string: ").upper()

str_1 = str_1.replace(" ", "")
str_2 = str_2.replace(" ", "")
listed_1 = sorted(list(str_1))
listed_2 = sorted(list(str_2))

strg_1 = str(listed_1)
strg_2 = str(listed_2)

if strg_1 == strg_2:   # if len(strg_1) > 0 and strg_1 == strg_2: (is an option)
    print("Anagrams")
else:
    print("Not anagrams")
