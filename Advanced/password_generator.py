
import string
import secrets


def generate_password(length: int) -> str:
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


if __name__ == '__main__':
    print("✵✵✵ Welcome to Password Generator ✵✵✵")
    while True:
        try:
            password_length_str = input("\nEnter the length (or 0 to quit): ")
            if not password_length_str.isdigit():
                raise ValueError("\nInvalid password length. Please enter a positive integer.")
            password_length = int(password_length_str)
            if password_length == 0:
                break
            elif password_length < 0:
                raise ValueError("\nInvalid password length. Please enter a positive integer.")
        except ValueError as e:
            print(f"\n\u001b[3m** Problem is: \u001b[38;5;196m{e}\u001b[0m")
            continue

        password = generate_password(password_length)
        print(f"\n\u001b[38;5;3;3mPassword: \u001b[38;5;27m{password}\u001b[0m")

        while True:
            try:
                response = input("\nWould you like another password? (y/n): ")
                if response.upper() not in ['Y', 'N']:
                    raise ValueError("\nInvalid response. Please enter Y or N.")
            except ValueError as e:
                print(f"\n\u001b[3m** Problem is: \u001b[38;5;196m{e}\u001b[0m")
                continue
            if response.upper() == 'N':
                break
            else:
                break

    print("\nThanks for using the Password Generator. Goodbye!")
