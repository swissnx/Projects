
import random


class PasswordGenerator:
    def __init__(self):
        self.__characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?-_=+[{]}\\|;:'\",<.>/?`~"

    def __generate_password(self, passlen: int) -> str:
        password = "".join(random.sample(self.__characters, passlen))
        return password

    def run(self):
        try:
            passlen = int(input("Pass Length: "))
            password = self.__generate_password(passlen)
            print(f"Generated: \u001b[38;5;51m{password}\u001b[0m\n")

            while True:
                prompt = input("\nTry again? (y/n): ")

                if prompt.lower() == "n":
                    break
                elif prompt.lower() == "y":
                    password = self.__generate_password(passlen)
                    print(f"Generated: \u001b[38;5;51m{password}\u001b[0m\n")

        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")


if __name__ == "__main__":
    generator = PasswordGenerator()
    generator.run()
