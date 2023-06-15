
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
