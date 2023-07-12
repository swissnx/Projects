
from os import path, system, mkdir
import hashlib


class HexBox:
    def __init__(self):
        self.__control_panel_name = 'Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}'
        self.__password_hash = None
        self.__folder_name = None

    def __create(self, folder_name: str, password: str):
        try:
            self.__password_hash = hashlib.sha256(password.encode()).hexdigest()
            self.__folder_name = folder_name
            if not path.exists(folder_name):
                mkdir(folder_name)
                return f'\n{folder_name} Created'
            else:
                raise FileExistsError(f'{folder_name} already exists')
            
        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def create(self, folder_name: str, password: str):
        return self.__create(folder_name, password)

    def __lock(self, folder_name: str):
        try:
            if path.exists(folder_name):
                system(f'ren "{folder_name}" "{self.__control_panel_name}"')
                system(f'attrib +h +s +r "{self.__control_panel_name}"')
                return '\nLocked!'
            else:
                raise FileNotFoundError(f'\n{folder_name} does not exist')
            
        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"
    
    def lock(self, folder_name: str):
        return self.__lock(folder_name)

    def __unlock(self, folder_name: str, password: str):
        try:
            if hashlib.sha256(password.encode()).hexdigest() == self.__password_hash and folder_name == self.__folder_name:
                if path.exists(self.__control_panel_name):
                    system(f'attrib -h -s -r "{self.__control_panel_name}"')
                    system(f'ren "{self.__control_panel_name}" "{folder_name}"')
                    return '\nUnlocked!'
                else:
                    raise FileNotFoundError(f'\n{folder_name} does not exist')
            else:
                return '\nIncorrect password or folder name'
            
        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def unlock(self, folder_name: str, password: str):
        return self.__unlock(folder_name, password)

    def __run(self):
        try:
            while True:
                print("\n1. Create Secret Folder\n2. Lock\n3. Unlock\n0. Exit")
                choice = input('\nChoice: ')

                if choice == '1':
                    folder_name = input('\nSet Folder Name: ')
                    password = input('Set Password: ')
                    try:
                        print(self.__create(folder_name, password))
                    except FileExistsError as fee:
                        print(fee)

                elif choice == '2':
                    folder_name = input('\nFolder Name: ')
                    try:
                        print(self.__lock(folder_name))
                    except FileNotFoundError as fnfe:
                        print(fnfe)

                elif choice == '3':
                    folder_name = input('\nFolder Name: ')
                    password = input('Password: ')
                    try:
                        print(self.__unlock(folder_name, password))
                    except FileNotFoundError as fnfe:
                        print(fnfe)

                elif choice == '0' or choice == "":
                    break
                
        except ValueError as ve:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{ve}\033[0m"

        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def run(self):
        return self.__run()


if __name__ == "__main__":
    hexbox = HexBox()
    hexbox.run()



# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ DOCUMENTATION ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #
# A secret hidden safebox for Windows to hide your contents
# Create, lock and unlock a secret folder on your computer.