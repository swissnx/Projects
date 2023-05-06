
from source.password_generator import generate_password
from source.file_encryption import encrypt_file
from source.file_decryption import decrypt_file


def aes_app():
    while True:
        print("\nOptions:")
        print("1. Generate a random password")
        print("2. Encrypt a file")
        print("3. Decrypt a file")
        print("4. Exit")
        choice = input("\nEnter your choice: ")

        if choice == '1':
            try:
                passlen = int(input("\nEnter the length of password: "))
                password = generate_password(passlen)
                print(f"\nPassword: \u001b[38;5;20m{password}\u001b[0m")

            except Exception as e:
                print(f"\nProblem is: {e}")

        elif choice == '2':
            try:
                file_path = input("\nEnter file path here: ")
                password = input("\nEnter Password to encrypt: ")
                encrypt_file(file_path, password)

            except Exception as e:
                print(f"\nProblem is: {e}")

        elif choice == '3':
            try:
                file_path = input("\nEnter file path here: ")
                password = input("\nEnter Password to decrypt: ")
                decrypt_file(file_path + '.enc', password)

            except Exception as e:
                print(f"\nProblem is: {e}")

        elif choice == '4':
            break

        else:
            print("\nInvalid choice. Please try again.")

if __name__ == '__main__':
    aes_app()
