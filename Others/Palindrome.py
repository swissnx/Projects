
class Palindrome:
    def __init__(self):
        pass

    @staticmethod
    def __palindrome(sentence: str) -> list:
        sentence = ''.join(c for c in sentence if c.isalnum() or c.isspace())
        words = sentence.split()
        palindromes = [word.lower() for word in words if word.lower() == word.lower()[::-1]]
        return palindromes

    @staticmethod
    def __check_palindrome(user_input):
        result = Palindrome.__palindrome(user_input)
        if result:
            print(f"{user_input} is a Palindrome word")
        else:
            print(f"{user_input} is not a Palindrome word")

    @staticmethod
    def __run():
        try:
            user_input = input("Enter a word to check: ")
            Palindrome.__check_palindrome(user_input)

            while True:
                prompt = input("\nTry again? (y/n): ")

                if prompt.lower() == "n":
                    break
                elif prompt.lower() == "y":
                    user_input = input("\nEnter a word to check: ")
                    Palindrome.__check_palindrome(user_input)
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

    @staticmethod
    def run():
        return Palindrome.__run()


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
