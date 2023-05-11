
from password_generator import generate_password, save_to_excel, save_to_text_file


try:
    passlen = int(input("\nPasslen: "))

    print("\nOptions:")
    print("1. All mixed")
    print("2. Letters only")
    print("3. Digits only")
    print("4. Special Characters only")
    print("5. Letters + Digits")
    print("6. Letters + Special Characters")
    print("7. Digits + Special Characters")

    characters = input("\nChoice: ")
    password = generate_password(passlen, characters)
    print(f"\n\u001b[38;5;3;3mPassword: \u001b[38;5;27m{password}\u001b[0m")

    save_to_excel(password)
    save_to_text_file(password)
    
except Exception as e:
    print(f"\n\u001b[3m** Problem is: \u001b[38;5;196m{e}\u001b[0m")

