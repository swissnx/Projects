
import subprocess


class macOSKeychain:
    def __init__(self):
        pass

    def __create_new(self, key, value):
        try:
            subprocess.run(['security', 'add-generic-password', '-a', key, '-s', key, '-w', value], check=True)

        except subprocess.CalledProcessError as e:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")

    def create_new(self, key, value):
        return self.__create_new(key, value)

    def __update(self, key, value):
        try:
            subprocess.run(['security', 'add-generic-password', '-a', key, '-s', key, '-w', value, '-U'], check=True)

        except subprocess.CalledProcessError as e:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")

    def update(self, key, value):
        return self.__update(key, value)

    def __retrieve_key(self, key):
        try:
            result = subprocess.run(['security', 'find-generic-password', '-a', key, '-s', key, '-w'], stdout=subprocess.PIPE, check=True)
            return result.stdout.decode('utf-8').strip()
        
        except subprocess.CalledProcessError as e:
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
    macOS_keychain = macOSKeychain()
    macOS_keychain.run()
