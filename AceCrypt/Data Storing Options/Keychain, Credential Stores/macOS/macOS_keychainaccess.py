
import KeychainAccess


class macOSKeychain:
    def __init__(self):
        self.keychain = KeychainAccess.Keychain(service='myService')

    def __create_new(self, key, value):
        self.keychain.set(key, value)

    def create_new(self, key, value):
        return self.__create_new(key, value)

    def __update(self, key, value):
        self.keychain.set(key, value)

    def update(self, key, value):
        return self.__update(key, value)

    def __retrieve_key(self, key):
        return self.keychain.get(key)

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
                        value = input("New Value: ")
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
    macOS_keychain = macOSKeychain()
    macOS_keychain.run()
