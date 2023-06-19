
from password_tools import PasswordTools


try:
    passtools = PasswordTools()
    passtools.run()

except Exception as e:
    print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")
