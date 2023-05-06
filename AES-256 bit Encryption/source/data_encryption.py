
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Protocol.KDF import PBKDF2
import os

def encrypt_data(data: bytes, password: str) -> bytes:
    """Encrypt data using AES-256 encryption with the given password."""
    salt = os.urandom(16)
    key = PBKDF2(password, salt, dkLen=32)
    cipher = AES.new(key, AES.MODE_CBC)
    encrypted_data = cipher.iv + cipher.encrypt(pad(data, AES.block_size))
    return salt + encrypted_data
