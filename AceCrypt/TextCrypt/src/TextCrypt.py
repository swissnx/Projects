
import base64
import binascii
import codecs
import crcmod.predefined
import hashlib


class ASCIIEncoder:
    def __init__(self):
        pass

    @staticmethod
    def __textEnc(message):
        try:
            if message == "":
                raise ValueError("Message cannot be empty")

            ascii_enc = ' '.join(str(ord(char)) for char in message)
            binary_enc = " ".join(format(ord(x), 'b') for x in message)
            octal_enc = " ".join("" + oct(ord(c))[2:] for c in message)
            hex_enc = binascii.hexlify(message.encode()).decode().upper()
            base64_enc = base64.b64encode(message.encode()).decode()

            return ascii_enc, binary_enc, octal_enc, hex_enc, base64_enc

        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    @staticmethod
    def textEnc(message):
        return ASCIIEncoder.__textEnc(message)


class ASCIIDecoder:
    def __init__(self):
        pass

    @staticmethod
    def ascii_dec(message):
        try:
            return ''.join(chr(int(x)) for x in message.split())
        except ValueError:
            return None

    @staticmethod
    def binary_dec(message):
        try:
            return ''.join(chr(int(x, 2)) for x in message.split())
        except ValueError:
            return None

    @staticmethod
    def octal_dec(message):
        try:
            return ''.join(chr(int(x, 8)) for x in message.split())
        except ValueError:
            return None

    @staticmethod
    def hex_dec(message):
        try:
            return codecs.decode(message, 'hex').decode()
        except binascii.Error:
            return None

    @staticmethod
    def base64_dec(message):
        try:
            return base64.b64decode(message).decode()
        except binascii.Error:
            return None


class HashEncoder:
    def __init__(self):
        pass

    @staticmethod
    def __textHash(message):
        try:
            if message == "":
                raise ValueError("Message cannot be empty")

            crc32_hash = crcmod.predefined.Crc('crc-32')
            crc32_hash.update(message.encode())
            crc32_enc = format(crc32_hash.crcValue, '08x')

            md5_enc = hashlib.md5(message.encode()).hexdigest()

            sha1_enc = hashlib.sha1(message.encode()).hexdigest()

            sha256_enc = hashlib.sha256(message.encode()).hexdigest()

            sha3_256_enc = hashlib.sha3_256(message.encode()).hexdigest()

            sha3_512_enc = hashlib.sha3_512(message.encode()).hexdigest()

            sha384_enc = hashlib.sha384(message.encode()).hexdigest()

            sha512_enc = hashlib.sha512(message.encode()).hexdigest()

            blake2_enc = hashlib.blake2s(message.encode()).hexdigest()

            return crc32_enc, md5_enc, sha1_enc, sha256_enc, sha3_256_enc, sha3_512_enc, sha384_enc, sha512_enc, blake2_enc

        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    @staticmethod
    def textHash(message):
        return HashEncoder.__textHash(message)


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


class UTFLengthFinder:
    def __init__(self):
        pass

    @staticmethod
    def __len_encoding(message):
        try:
            if message == "":
                raise ValueError("Message cannot be empty")

            try:
                utf_8 = len(message.encode('utf-8'))
            except UnicodeDecodeError:
                utf_8 = None

            try:
                utf_16 = len(message.encode('utf-16'))
            except UnicodeDecodeError:
                utf_16 = None

            try:
                utf_32 = len(message.encode('utf-32'))
            except UnicodeDecodeError:
                utf_32 = None

            return utf_8, utf_16, utf_32

        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    @staticmethod
    def len_encoding(message):
        return UTFLengthFinder.__len_encoding(message)


class TextCrypt:
    def __init__(self):
        self.__ascii_enc = ASCIIEncoder()
        self.__ascii_dec = ASCIIDecoder()
        self.__hash_enc = HashEncoder()
        self.__verify_hash = HashVerifier()
        self.__utf_len = UTFLengthFinder()

    def __run(self):
        while True:
            try:
                print("\n1. Encode Text\n2. Decode Text\n3. Verify Hash\n0. Exit")
                choice = input("\nChoice: ")

                if choice == "0" or choice == "":
                    break

                elif choice == "1":
                    print("\nMessage:")

                    message = ""

                    while True:
                        line = input()
                        if line == "END":
                            break
                        message += line + "\n"
                    message = message[:-1]

                    if message == "":
                        break

                    try:
                        ascii_enc, binary_enc, octal_enc, hex_enc, base64_enc = self.__ascii_enc.textEnc(message)
                        crc32_enc, md5_enc, sha1_enc, sha256_enc, sha3_256_enc, sha3_512_enc, sha384_enc, sha512_enc, blake2_enc = self.__hash_enc.textHash(message)
                        utf_8, utf_16, utf_32 = self.__utf_len.len_encoding(message)

                        print(f"\nASCII: {ascii_enc}")
                        print(f"\nBinary: {binary_enc}")
                        print(f"\nOctal: {octal_enc}")
                        print(f"\nHexadecimal: {hex_enc}")
                        print(f"\nBase64: {base64_enc}")
                        
                        print("\n-----------------------------")

                        print(f"\nCRC-32: {crc32_enc}")
                        print(f"\nMD5: {md5_enc}")
                        print(f"\nSHA-1: {sha1_enc}")
                        print(f"\nSHA-256: {sha256_enc}")
                        print(f"\nSHA-3-256: {sha3_256_enc}")
                        print(f"\nSHA-3-512: {sha3_512_enc}")
                        print(f"\nSHA-384: {sha384_enc}")
                        print(f"\nSHA-512: {sha512_enc}")
                        print(f"\nBLAKE2: {blake2_enc}")

                        print("\n-----------------------------")

                        if utf_8 is not None:
                            print(f"\nUTF-8 : {str(utf_8)} bytes")

                        if utf_16 is not None:
                            print(f"UTF-16: {str(utf_16)} bytes")

                        if utf_32 is not None:
                            print(f"UTF-32: {str(utf_32)} bytes")

                    except ValueError as ve:
                        return f"\n\033[3m!✶ Error: \033[38;5;200m{ve}\033[0m"


                elif choice == "2":
                    message = input("\nValue: ")

                    if message == "":
                        break

                    print("\nFrom:\n1. ASCII\n2. Binary\n3. Octal\n4. Hex\n5. Base64")
                    ascii_choice = input("\nChoice: ")

                    try:
                        if ascii_choice == "1":
                            ascii_dec = ASCIIDecoder.ascii_dec(message)
                            print(f"\nASCII: {ascii_dec}")
                        elif ascii_choice == "2":
                            binary_dec = ASCIIDecoder.binary_dec(message)
                            print(f"\nBinary: {binary_dec}")
                        elif ascii_choice == "3":
                            octal_dec = ASCIIDecoder.octal_dec(message)
                            print(f"\nOctal: {octal_dec}")
                        elif ascii_choice == "4":
                            hex_dec = ASCIIDecoder.hex_dec(message)
                            print(f"\nHexadecimal: {hex_dec}")
                        elif ascii_choice == "5":
                            base64_dec = ASCIIDecoder.base64_dec(message)
                            print(f"\nBase64: {base64_dec}")

                    except ValueError as ve:
                        return f"\n\033[3m!✶ Error: \033[38;5;200m{ve}\033[0m"


                elif choice == "3":
                    message = input("\nMessage: ")
                    print("\n1. CRC-32\n2. MD5\n3. SHA-1\n4. SHA-256\n5. SHA-3-256\n6. SHA-3-512\n7. SHA-384\n8. SHA-512\n9. BLAKE2\n0. Exit")
                    algorithm_number = input("\nAlgorithm: ")

                    if algorithm_number == "0" or algorithm_number == "":
                        break
                    
                    algorithm = self.__verify_hash.get_algorithm(algorithm_number)

                    print(f"\nVerifying {algorithm} hash value...")

                    hash_value = input(f"\nEnter {algorithm} hash: ")

                    if self.__verify_hash.verify(message, hash_value, algorithm):
                        print("\033[38;5;207mThey Match!\033[0m")
                    else:
                        print("\033[38;5;172mThey Do Not Match.\033[0m")


            except ValueError as ve:
                return f"\n\033[3m!✶ Error: \033[38;5;200m{ve}\033[0m"
            
            except Exception as e:
                return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def run(self):
        return self.__run()


if __name__ == "__main__":
    textcrypt = TextCrypt()
    textcrypt.run()
