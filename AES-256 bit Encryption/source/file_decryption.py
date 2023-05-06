
from source.data_decryption import decrypt_data

def decrypt_file(file_path: str, password: str) -> None:
    """Decrypt a file encrypted with AES-256 encryption using the given password."""
    with open(file_path, 'rb') as f:
        encrypted_data = f.read()
    decrypted_data = decrypt_data(encrypted_data, password)
    with open(file_path[:-4], 'wb') as f:
        f.write(decrypted_data)
