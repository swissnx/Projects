
# A palindrome is a word or a phrase that is the same whether you read it backwards or forwards, for example the word ' refer'.

def palindrome(sentence: str) -> list:
    sentence = ''.join(c for c in sentence if c.isalnum() or c.isspace())
    words = sentence.split()
    palindromes = [word.lower() for word in words if word.lower() == word.lower()[::-1]]
    return palindromes

try:
    user_input = input("Enter a word to check: ")
    result = palindrome(user_input)

    if result:
        print(f"{user_input} is a Palindrome word")
    else:
        print(f"{user_input} is not a Palindrome word")
    
    while True:
        prompt = input("\nTry again? (y/n): ")
      
        if prompt.lower() == "n":
            break
        elif prompt.lower() == "y":
            user_input = input("\nEnter a word to check: ")
            result = palindrome(user_input)
            
            if result:
                print(f"{user_input} is a Palindrome word")
            else:
                print(f"{user_input} is not a Palindrome word")

except Exception as e:
    print(f"\nProblem is: {e}")
