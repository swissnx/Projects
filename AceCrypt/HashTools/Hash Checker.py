
import hashlib


class FileHash:
    def __init__(self):
        self.__file_path = ''
        self.__file_hash = ''
        self.__user_hash = ''

    def __generate_file_hash(self):
        try:
            with open(self.__file_path, 'rb') as f:
                file_data = f.read()
                self.__file_hash = hashlib.sha256(file_data).hexdigest()
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

    def generate_file_hash(self):
        return self.__generate_file_hash()

    def __compare_hashes(self):
        if self.__file_hash.upper() == self.__user_hash.upper():
            print('\u001b[38;5;207mThey match!\u001b[0m')
        else:
            print('\u001b[38;5;172mThey do not match.\u001b[0m')

    def compare_hashes(self):
        return self.__compare_hashes()

    def __run(self):
        try:
            self.__file_path = input('Enter the file path: ')
            self.__generate_file_hash()
            print(f'SHA-256 File Hash: \u001b[38;5;33m{self.__file_hash.upper()}\u001b[0m')

            self.__user_hash = input('Target: ')
            self.__compare_hashes()
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

    def run(self):
        return self.__run()


if __name__ == "__main__":
    file_hash = FileHash()
    file_hash.run()
