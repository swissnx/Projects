
#pip install better_profanity

from better_profanity import profanity


user = input("Enter text with profanity to test: ")
censored = profanity.censor(user)

print(censored)
