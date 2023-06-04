
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




# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ DOCUMENTATION ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #
""" Let's play a game. We will give you two strings: one being a word (e.g., "dog") and the second being a combination of any characters.
Your task is to write a program which answers the following question: are the characters comprising the first string hidden inside the second string?

For example:
   • if the second string is given as "vcxzxduybfdsobywuefgas", the answer is yes;
   • if the second string is "vcxzxdcybfdstbywuefsas", the answer is no (as there are neither the letters "d", "o", or "g", in this order)

Hints:
   • you should use the two-argument variants of the pos() functions inside your code;
   • don't worry about case sensitivity.   """


word = input("Enter the word you wish to find: ").upper()
strn = input("Enter the string you wish to search through: ").upper()

found = True
start = 0

for ch in word:
	pos = strn.find(ch, start)  # find() method returns the index of the first occurrence of the specified character in the string or returns -1 if the character is not found.
	if pos < 0:                # If pos is greater than or equal to 0,
		found = False
		break
	start = pos + 1     # the code updates the value of start to pos + 1 and continues the loop.
if found:
	print("Yes")
else:
	print("No")



#***************************  *************************** ***************************

# The line pos = strn.find(ch, start) is using the find method to search for the character ch in the string strn, starting from the index start.

word = "HELLO"
strn = "HELLO WORLD"

found = True
start = 0

for ch in word:
	pos = strn.find(ch, start) 
	if pos < 0:
		found = False
		break
	start = pos + 1
if found:
	print("Yes")
else:
	print("No")


# In this example, the word to find is 'HELLO' and the string to search through is 'HELLO WORLD'. The 'found' variable is set to True and the 'start' variable
# is set to 0. The 'for' loop iterates through each character in the 'word' variable. On the first iteration, 'ch' is 'H'. The 'find' method is called to search
# for the first occurrence of 'H' in 'strn', starting from index '0'. The method returns the index '0', which is stored in the 'pos' variable. The 'start' variable
# is then updated to 'pos + 1 = 0 + 1 = 1'. The loop continues until all characters in 'word' have been searched for in 'strn'. If all characters are found,
# the 'found' variable remains True and the code prints "Yes". If any of the characters are not found, the 'found' method returns '-1', the 'found' variable
# is set to False, and the loop breaks. In this case, the code would print "No".

