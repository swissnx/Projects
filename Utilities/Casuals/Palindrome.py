
class Palindrome:
    def __init__(self):
        pass

    @staticmethod
    def __palindrome(sentence: str) -> bool:
        sentence = ''.join(c for c in sentence if c.isalnum() or c.isspace())
        words = sentence.split()
        return any(word.lower() == word.lower()[::-1] for word in words)

    @staticmethod
    def run():
        while True:
            try:
                prompt = input("\nPalindrome Word: ")
                result = Palindrome.__palindrome(prompt)

                if prompt == "":
                    break

                if result == True:
                    print(f"\n{prompt}: Positive")
                elif result == False:
                    print(f"\n{prompt}: Negative")
                else:
                    print("Invalid input")

            except Exception as e:
                print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")


if __name__ == "__main__":
    palindrome = Palindrome()
    palindrome.run()



# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ DOCUMENTATION ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #
# A palindrome is a word or a phrase that is the same whether you read it backwards or forwards, for example the word ' refer'.

"""   It's a word which look the same when read forward and backward. For example, "kayak" is a palindrome, while "loyal" is not.
Your task is to write a program which:
   • asks the user for some text;
   • checks whether the entered text is a palindrome, and prints result.

Note:
   • assume that an empty string isn't a palindrome;
   • treat upper- and lower-case letters as equal;
   • spaces are not taken into account during the check - treat them as non-existent;
   • there are more than a few correct solutions - try to find more than one.

Test:
   Ten animals I slam in a net
   Eleven animals I slam in a net                  """

text = input("Enter text: ")

text = text.replace(' ','')    # remove all spaces...

if len(text) > 1 and text.upper() == text[::-1].upper():   # ... and check if the word is equal to reversed itself
	print("It's a palindrome")
else:
	print("It's not a palindrome")
