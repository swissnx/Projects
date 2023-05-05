
import random


def generate_password(passlen: int) -> str:
    characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?-_=+[{]}\\|;:'\",<.>/?`~"
    password = "".join(random.sample(characters, passlen))
    return password


try:
    passlen = int(input("Length of password: "))
    password = generate_password(passlen)
    print(f"Generated password: \u001b[38;5;51m{password}\u001b[0m\n")

    while True:
        prompt = input("\nTry again? (y/n): ")
      
        if prompt.lower() == "n":
            break
        elif prompt.lower() == "y":
            password = generate_password(passlen)
            print(f"Generated password: \u001b[38;5;51m{password}\u001b[0m\n")

except Exception as e:
    print(f"\nProblem is: {e}\n")
