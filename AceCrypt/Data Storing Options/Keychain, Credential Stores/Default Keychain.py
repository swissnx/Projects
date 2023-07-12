
import keyring


class KeyStore:
    def __init__(self):
        self.__system = "my_system"

    def __create_new(self, key, value):
        try:
            keyring.set_password(self.__system, key, value)

        except Exception as e:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")

    def create_new(self, key, value):
        return self.__create_new(key, value)

    def __update(self, key, value):
        try:
            keyring.set_password(self.__system, key, value)

        except Exception as e:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")

    def update(self, key, value):
        return self.__update(key, value)

    def __retrieve_key(self, key):
        try:
            return keyring.get_password(self.__system, key)
        
        except Exception as e:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")

    def retrieve_key(self, key):
        return self.__retrieve_key(key)

    def run(self):
        while True:
            print("\n1. Create New\n2. Update\n3. Retrieve Key\n0. Exit")

            try:
                action = input("\nAction: ")

                if action.isalpha():
                    print("Invalid input. Please enter an integer.")
                
                else:
                    action = int(action)

                    if action == 1:
                        key = input("Key: ")
                        value = input("Value: ")
                        self.create_new(key, value)
                        print("\nKeychain created!")

                    elif action == 2:
                        key = input("Key: ")
                        value = input("Value: ")
                        self.update(key, value)
                        print("\nKeychain updated!")

                    elif action == 3:
                        key = input("Key: ")
                        print(f"\nValue: {self.retrieve_key(key)}")

                    elif action == 0 or action == "":
                        break

            except ValueError as ve:
                return f"\n\033[3m!✶ Error: \033[38;5;200m{ve}\033[0m"

            except Exception as e:
                return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"


if __name__ == "__main__":
    keystore = KeyStore()
    keystore.run()
