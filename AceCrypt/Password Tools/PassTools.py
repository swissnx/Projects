
from password_tools import PasswordTools


try:
    passtools = PasswordTools()
    passtools.run()

except Exception as e:
    print(f"\n\u001b[3m✶!✶ Error: \u001b[38;5;200m{e}\u001b[0m")
