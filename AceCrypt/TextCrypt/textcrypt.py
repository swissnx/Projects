
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from TextCrypt import TextCrypt

try:
    textcrypt = TextCrypt()
    textcrypt.run()
except Exception as e:
    print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")
