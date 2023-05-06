
from source.data_encryption import encrypt_data

def encrypt_file(file_path: str, password: str) -> None:
    """Encrypt a file using AES-256 encryption with the given password."""
    with open(file_path, 'rb') as f:
        data = f.read()
    encrypted_data = encrypt_data(data, password)
    with open(file_path + '.enc', 'wb') as f:
        f.write(encrypted_data)
