
import keyring


class WinCredentialStore:
    def __init__(self):
        self.__key = None
        self.__value = None

    def __get_credentials(self):
        try:
            keyring.set_password("my_system", self.__key, self.__value)

        except Exception as e:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")

    def get_credentials(self):
        return self.__get_credentials()

    def __update_credentials(self):
        try:
            keyring.set_password("my_system", self.__key, self.__value)

        except Exception as e:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")

    def update_credentials(self):
        return self.__update_credentials()

    def __retrieve_credentials(self):
        try:
            self.__value = keyring.get_password("my_system", self.__key)

            if not self.__value:
                return "\nCredentials not found!"
            
        except Exception as e:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")

    def retrieve_credentials(self):
        return self.__retrieve_credentials()

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
                        self.__key = input("Key: ")
                        self.__value = input("Value: ")
                        self.get_credentials()
                        print("\nCredentials stored!")

                    elif action == 2:
                        self.__key = input("Key: ")
                        self.__value = input("Value: ")
                        self.update_credentials()
                        print("\nCredentials updated!")

                    elif action == 3:
                        self.__key = input("Key: ")
                        self.retrieve_credentials()
                        print(f"\nValue: {self.__value}")

                    elif action == 0 or action == "":
                        break
                    
                    else:
                        print("\nInvalid option!")

            except ValueError as ve:
                return f"\n\033[3m!✶ Error: \033[38;5;200m{ve}\033[0m"

            except Exception as e:
                return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"


if __name__ == "__main__":
    wincred_store = WinCredentialStore()
    wincred_store.run()
