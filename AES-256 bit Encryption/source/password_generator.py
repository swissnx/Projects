
import string
import secrets


def generate_password(length: int) -> str:
    """Generate a random password of the given length using a cryptographically secure random number generator."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password
