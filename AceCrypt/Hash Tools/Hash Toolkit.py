
import os
import json
import hashlib
import whirlpool       #pip install whirlpool
from datetime import datetime as dt


class HashToolkit:
    def __init__(self):
        self.__path = None
        self.__hash_type = None
        self.__log_file_path = 'hash_log.json'

    def __generate_hash(self, hash_type: str):
      try:
          if os.path.isfile(self.__path):
              file_hash = HashToolkit.__generate_hash_for_file(self.__path, hash_type)
              self.save_hash_values(self.__log_file_path, file_hash)
              return file_hash
          elif os.path.isdir(self.__path):
              file_hashes = {}
              for root, dirs, files in os.walk(self.__path):
                  for file in files:
                      file_path = os.path.join(root, file)
                      file_hash = HashToolkit.__generate_hash_for_file(file_path, hash_type)
                      file_hashes[file_path] = file_hash
              self.save_hash_values(self.__log_file_path, file_hashes)
              return file_hashes
      except Exception as e:
          return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def generate_hash(self, hash_type: str):
        try:
            return self.__generate_hash(hash_type)
        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

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
                elif hash_type == 'sha3_512':
                    hasher = hashlib.sha3_512()
                elif hash_type == 'sha384':
                    hasher = hashlib.sha384()
                elif hash_type == 'sha512':
                    hasher = hashlib.sha512()
                elif hash_type == 'blake2s':
                    hasher = hashlib.blake2s()
                # elif hash_type == 'whirlpool':
                #     hasher = whirlpool.new()

                buf = f.read(BLOCKSIZE)
                while len(buf) > 0:
                    hasher.update(buf)
                    buf = f.read(BLOCKSIZE)
                return hasher.hexdigest()
        except Exception as e:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")
            return None

    @staticmethod
    def generate_hash_for_file(file_path: str, hash_type: str):
        try:
            return HashToolkit.__generate_hash_for_file(file_path, hash_type)
        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def __verify_hash(self, target_hash: str, hash_type: str):
        try:
            file_hash = self.__generate_hash(hash_type)
            if isinstance(file_hash, dict):
                match = all(target_hash.upper() == h.upper() for h in file_hash.values())
            else:
                match = file_hash.upper() == target_hash.upper()
            self.save_hash_values(self.__log_file_path, file_hash)
            return match

        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def verify_hash(self, path: str, target_hash: str, hash_type: str):
        try:
            self.__path = path
            return self.__verify_hash(target_hash, hash_type)
        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

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
                return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    @staticmethod
    def get_valid_option(prompt: str, options: list):
        try:
            return HashToolkit.__get_valid_option(prompt, options)
        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def __save_hash_values(self, file_path: str, hash_values):
        try:
            data = {'datetime': dt.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'file_path': self.__path,
                    'hash_algorithm': self.__hash_type,
                    'hash_values': hash_values
                    }
            try:
                with open(file_path, 'r') as f:
                    existing_data = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                existing_data = []
            existing_data.append(data)
            with open(file_path, 'w') as f:
                json.dump(existing_data, f, indent=4)
        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def save_hash_values(self, file_path: str, hash_values):
        return self.__save_hash_values(file_path, hash_values)

    def __load_hash_values(self, file_path: str):
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            self.__path = data['file_path']
            self.__hash_type = data['hash_algorithm']
            return data['hash_values']
        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def load_hash_values(self, file_path: str):
        return self.__load_hash_values(file_path)

    def __run(self):
        self.__path = input('File/Dir Path: ')

        while True:
            try:
                print("\nOptions:\n1. Generate\n2. Verify\n3. Change Path\n4. Exit")

                option = HashToolkit.__get_valid_option("\nChoice: ", ['1', '2', '3', '4'])

                if option == "1":
                    print("\nHash Types:\n1. MD5\n2. SHA-1\n3. SHA-256\n4. SHA-3_256\n5. SHA-3_512\n6. SHA-384\n7. SHA-512\n8. BLAKE2\n9. Whirlpool")
                    hash_type = HashToolkit.__get_valid_option("\nHash type: ", ['1', '2', '3', '4', '5', '6', '7', '8', '9'])

                    if hash_type == '1':
                        self.__hash_type = 'md5'
                        file_hash = self.__generate_hash('md5')

                    elif hash_type == '2':
                        self.__hash_type = 'sha1'
                        file_hash = self.__generate_hash('sha1')

                    elif hash_type == '3':
                        self.__hash_type = 'sha256'
                        file_hash = self.__generate_hash('sha256')

                    elif hash_type == '4':
                        self.__hash_type = 'sha3_256'
                        file_hash = self.__generate_hash('sha3_256')

                    elif hash_type == '5':
                        self.__hash_type = 'sha3_512'
                        file_hash = self.__generate_hash('sha3_512')

                    elif hash_type == '6':
                        self.__hash_type = 'sha384'
                        file_hash = self.__generate_hash('sha384')

                    elif hash_type == '7':
                        self.__hash_type = 'sha512'
                        file_hash = self.__generate_hash('sha512')

                    elif hash_type == '8':
                        self.__hash_type = 'blake2s'
                        file_hash = self.__generate_hash('blake2s')

                    elif hash_type == '9':
                        self.__hash_type = 'whirlpool'
                        file_hash = self.__generate_hash('whirlpool')

                    if isinstance(file_hash, dict):
                        for file_path, h in file_hash.items():
                            print(f'{file_path}: \033[38;5;33m{h.upper()}\033[0m')
                    else:
                        print(f'File Hash: \033[38;5;33m{file_hash.upper()}\033[0m')

                elif option == "2":
                    print("\nHash Types:\n1. MD5\n2. SHA-1\n3. SHA-256\n4. SHA-3_256\n5. SHA-3_512\n6. SHA-384\n7. SHA-512\n8. BLAKE2\n9. Whirlpool")

                    hash_type = HashToolkit.__get_valid_option("\nHash type: ", ['1', '2', '3', '4', '5', '6', '7', '8', '9'])

                    user_hash = input("Target Hash: ")

                    if hash_type == '1':
                        self.__hash_type = 'md5'
                        match = self.__verify_hash(user_hash, 'md5')

                    elif hash_type == '2':
                        self.__hash_type = 'sha1'
                        match = self.__verify_hash(user_hash, 'sha1')

                    elif hash_type == '3':
                        self.__hash_type = 'sha256'
                        match = self.__verify_hash(user_hash, 'sha256')

                    elif hash_type == '4':
                        self.__hash_type = 'sha3_256'
                        match = self.__verify_hash(user_hash, 'sha3_256')

                    elif hash_type == '5':
                        self.__hash_type = 'sha3_512'
                        match = self.__verify_hash(user_hash, 'sha3_512')

                    elif hash_type == '6':
                        self.__hash_type = 'sha384'
                        match = self.__verify_hash(user_hash, 'sha384')

                    elif hash_type == '7':
                        self.__hash_type = 'sha512'
                        match = self.__verify_hash(user_hash, 'sha512')

                    elif hash_type == '8':
                        self.__hash_type = 'blake2s'
                        match = self.__verify_hash(user_hash, 'blake2s')

                    elif hash_type == '9':
                        self.__hash_type = 'whirlpool'
                        match = self.__verify_hash(user_hash, 'whirlpool')

                    if match:
                        print("\033[38;5;207mThey Match!\033[0m")
                    else:
                        print("\033[38;5;172mThey Do Not Match.\033[0m")

                elif option == "3":
                    self.__path = input('New Path: ')

                elif option == "4":
                    break
                
            except Exception as e:
                return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def run(self):
        try:
            return self.__run()
        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"


if __name__ == "__main__":
    hash_tools = HashToolkit()
    hash_tools.run()
