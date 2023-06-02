
from password_generator import PasswordGenerator

try:
    passgen = PasswordGenerator()
    passgen.run()

except Exception as e:
    print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")
