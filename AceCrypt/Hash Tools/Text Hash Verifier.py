
import crcmod.predefined
import hashlib


class HashVerifier:
    def __init__(self):
        pass

    @staticmethod
    def __crc32(message: str) -> str:
        crc32_hash = crcmod.predefined.Crc('crc-32')
        crc32_hash.update(message.encode())
        crc32_enc = format(crc32_hash.crcValue, '08x')

        return crc32_enc

    @staticmethod
    def __md5(message: str) -> str:
        md5_hash = hashlib.md5(message.encode()).hexdigest()
        
        return md5_hash

    @staticmethod
    def __verify(message: str, hash_value: str, algorithm: str) -> bool:
        if algorithm == "crc32":
            calculated_hash_value = HashVerifier.__crc32(message)

        elif algorithm == "md5":
            calculated_hash_value = HashVerifier.__md5(message)

        else:
            calculated_hash_value = hashlib.new(algorithm, message.encode()).hexdigest()

        return calculated_hash_value == hash_value

    @staticmethod
    def verify(message: str, hash_value: str, algorithm: str) -> bool:
        return HashVerifier.__verify(message, hash_value, algorithm)

    @staticmethod
    def __get_algorithm(algorithm_number: str) -> str:
        # Map the entered number to the corresponding algorithm name
        algorithms = ["crc32", "md5", "sha1", "sha256", "sha3_256", "sha3_512", "sha384", "sha512", "blake2s"]
        try:
            algorithm = algorithms[int(algorithm_number) - 1]

        except (IndexError, ValueError):
            raise ValueError("Invalid algorithm number")
        
        return algorithm

    @staticmethod
    def get_algorithm(algorithm_number: str) -> str:
        return HashVerifier.__get_algorithm(algorithm_number)

    def run(self):
        try:
            while True:
                message = input("\nMessage: ")

                print("\n1. CRC-32\n2. MD5\n3. SHA-1\n4. SHA-256\n5. SHA-3-256\n6. SHA-3-512\n7. SHA-384\n8. SHA-512\n9. BLAKE2\n0. Exit")

                algorithm_number = input("\nAlgorithm: ")

                if algorithm_number == "0" or algorithm_number == "":
                    break

                algorithm = self.__get_algorithm(algorithm_number)

                print(f"\nVerifying {algorithm} hash value...")

                hash_value = input(f"\nEnter {algorithm} hash: ")

                if self.verify(message, hash_value, algorithm):
                    print("\033[38;5;207mThey Match!\033[0m")
                else:
                    print("\033[38;5;172mThey Do Not Match.\033[0m")

        except ValueError as ve:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{ve}\033[0m"
        
        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"


if __name__ == "__main__":
    verify_hash = HashVerifier()
    verify_hash.run()