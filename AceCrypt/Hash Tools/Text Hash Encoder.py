
import crcmod.predefined
import hashlib


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

    def run(self):
        try:
            message = input("Encode Message: ")
            crc32_enc, md5_enc, sha1_enc, sha256_enc, sha3_256_enc, sha3_512_enc, sha384_enc, sha512_enc, blake2_enc = self.textHash(message)

            print(f"\nCRC-32: {crc32_enc}")
            print(f"\nMD5: {md5_enc}")
            print(f"\nSHA-1: {sha1_enc}")
            print(f"\nSHA-256: {sha256_enc}")
            print(f"\nSHA-3-256: {sha3_256_enc}")
            print(f"\nSHA-3-512: {sha3_512_enc}")
            print(f"\nSHA-384: {sha384_enc}")
            print(f"\nSHA-512: {sha512_enc}")
            print(f"\nBLAKE2: {blake2_enc}")

        except ValueError as ve:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{ve}\033[0m"
        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"


if __name__ == "__main__":
    hash_text = HashEncoder()
    hash_text.run()