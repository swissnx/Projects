
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Protocol.KDF import PBKDF2

def decrypt_data(encrypted_data: bytes, password: str) -> bytes:
    """Decrypt data encrypted with AES-256 encryption using the given password."""
    salt = encrypted_data[:16]
    key = PBKDF2(password, salt, dkLen=32)
    cipher = AES.new(key, AES.MODE_CBC, iv=encrypted_data[16:32])
    decrypted_data = unpad(cipher.decrypt(encrypted_data[32:]), AES.block_size)
    return decrypted_data
