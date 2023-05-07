
from password_generator import generate_password


try:
    passlen = int(input("\nLength: "))
except Exception as e:
    print(f"\n\u001b[3m** Problem is: \u001b[38;5;196m{e}\u001b[0m")

password = generate_password(passlen)
print(f"\n\u001b[38;5;3;3mPassword: \u001b[38;5;27m{password}\u001b[0m")
