
import hashlib
import os


class HashGen:
    def __init__(self):
        self.__path = input('File / Directory Path: ')

    def __generate_file_hash(self, hash_type: str):
        try:
            if os.path.isfile(self.__path):
                return HashGen.__generate_hash_for_file(self.__path, hash_type)
            elif os.path.isdir(self.__path):
                file_hashes = {}
                for root, dirs, files in os.walk(self.__path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        file_hash = HashGen.__generate_hash_for_file(file_path, hash_type)
                        file_hashes[file_path] = file_hash
                return file_hashes
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

    def generate_file_hash(self, hash_type: str):
        try:
            return self.__generate_file_hash(hash_type)
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

    @staticmethod
    def __generate_hash_for_file(file_path: str, hash_type: str):
        BLOCKSIZE = 65536
        try:
            with open(file_path, 'rb') as f:
                if hash_type == 'md5':
                    hasher = hashlib.md5()
                elif hash_type == 'sha1':
                    hasher = hashlib.sha1()
                elif hash_type == 'sha256':
                    hasher = hashlib.sha256()
                elif hash_type == 'sha3_256':
                    hasher = hashlib.sha3_256()
                elif hash_type == 'sha384':
                    hasher = hashlib.sha384()
                elif hash_type == 'sha512':
                    hasher = hashlib.sha512()

                buf = f.read(BLOCKSIZE)
                while len(buf) > 0:
                    hasher.update(buf)
                    buf = f.read(BLOCKSIZE)
                return hasher.hexdigest()
        except Exception as e:
            print(f'\u001b[3mError generating hash for {file_path}: \u001b[38;5;200m{e}\u001b[0m')
            return None

    @staticmethod
    def generate_hash_for_file(file_path: str, hash_type: str):
        try:
            return HashGen.__generate_hash_for_file(file_path, hash_type)
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

    def __compare_hashes(self, target_hash: str, hash_type: str):
        try:
            file_hash = self.__generate_file_hash(hash_type)
            if isinstance(file_hash, dict):
                match = all(target_hash.upper() == h.upper() for h in file_hash.values())
            else:
                match = file_hash.upper() == target_hash.upper()
            return match
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

    def compare_hashes(self, target_hash: str, hash_type: str):
        try:
            return self.__compare_hashes(target_hash, hash_type)
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

    @staticmethod
    def __get_valid_option(prompt: str, options: list):
        while True:
            try:
                option = input(prompt)
                if option in options:
                    return option
                else:
                    print(f'Invalid option. Please enter one of the following options: {options}')
            except Exception as e:
                print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

    @staticmethod
    def get_valid_option(prompt: str, options: list):
        try:
            return HashGen.__get_valid_option(prompt, options)
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

    def __run(self):
        while True:
            try:
                print("\nOptions:\n1. Generate File Hash\n2. Compare Hashes\n3. Change Path\n4. Exit")
                option = HashGen.__get_valid_option("\nEnter your option: ", ['1', '2', '3', '4'])
                if option == "1":
                    print("\nHash Types:\n1. MD5\n2. SHA1\n3. SHA256\n4. SHA3_256\n5. SHA384\n6. SHA512")
                    hash_type = HashGen.__get_valid_option("\nEnter the hash type: ", ['1', '2', '3', '4', '5', '6'])
                    if hash_type == '1':
                        file_hash = self.__generate_file_hash('md5')
                    elif hash_type == '2':
                        file_hash = self.__generate_file_hash('sha1')
                    elif hash_type == '3':
                        file_hash = self.__generate_file_hash('sha256')
                    elif hash_type == '4':
                        file_hash = self.__generate_file_hash('sha3_256')
                    elif hash_type == '5':
                        file_hash = self.__generate_file_hash('sha384')
                    elif hash_type == '6':
                        file_hash = self.__generate_file_hash('sha512')

                    if isinstance(file_hash, dict):
                        for file_path, h in file_hash.items():
                            print(f'{file_path}: \u001b[38;5;33m{h.upper()}\u001b[0m')
                    else:
                        print(f'File Hash: \u001b[38;5;33m{file_hash.upper()}\u001b[0m')

                elif option == "2":
                    print("\nHash Types:\n1. MD5\n2. SHA1\n3. SHA256\n4. SHA3_256\n5. SHA384\n6. SHA512")
                    hash_type = HashGen.__get_valid_option("\nEnter the hash type: ", ['1', '2', '3', '4', '5', '6'])
                    user_hash = input('Target Hash: ')
                    if hash_type == '1':
                        match = self.__compare_hashes(user_hash, 'md5')
                    elif hash_type == '2':
                        match = self.__compare_hashes(user_hash, 'sha1')
                    elif hash_type == '3':
                        match = self.__compare_hashes(user_hash, 'sha256')
                    elif hash_type == '4':
                        match = self.__compare_hashes(user_hash, 'sha3_256')
                    elif hash_type == '5':
                        match = self.__compare_hashes(user_hash, 'sha384')
                    elif hash_type == '6':
                        match = self.__compare_hashes(user_hash, 'sha512')

                    if match:
                        print('\u001b[38;5;207mThey match!\u001b[0m')
                    else:
                        print('\u001b[38;5;172mThey do not match.\u001b[0m')

                elif option == "3":
                    self.__path = input('New File / Directory Path: ')

                elif option == "4":
                    break
            except Exception as e:
                print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

    def run(self):
        try:
            return self.__run()
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")


if __name__ == "__main__":
    hash_gen = HashGen()
    hash_gen.run()
