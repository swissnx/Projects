
from os import path, system, mkdir
import hashlib


class HexBox:
    def __init__(self):
        self.__control_panel_name = 'Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}'
        self.__password_hash = None
        self.__folder_name = None

    def __create(self):
        folder_name = input('\nSet Folder Name: ')
        password = input('Set Password: ')
        self.__password_hash = hashlib.sha256(password.encode()).hexdigest()
        self.__folder_name = folder_name
        if not path.exists(folder_name):
            mkdir(folder_name)
            return f'\n{folder_name} Created'
        else:
            return f'{folder_name} already exists'

    def create(self):
        return self.__create()

    def __lock(self):
        folder_name = input('\nEnter Folder Name: ')
        if path.exists(folder_name):
            system(f'ren "{folder_name}" "{self.__control_panel_name}"')
            system(f'attrib +h +s +r "{self.__control_panel_name}"')
            return '\nLocked!'
        else:
            return f'\n{folder_name} does not exist'
    
    def lock(self):
        return self.__lock()

    def __unlock(self):
        folder_name = input('\nEnter Folder Name: ')
        password = input('Enter Password: ')
        if hashlib.sha256(password.encode()).hexdigest() == self.__password_hash and folder_name == self.__folder_name:
            if path.exists(self.__control_panel_name):
                system(f'attrib -h -s -r "{self.__control_panel_name}"')
                system(f'ren "{self.__control_panel_name}" "{folder_name}"')
                return '\nUnlocked!'
            else:
                return f'\n{self.__control_panel_name} does not exist'
        else:
            return '\nIncorrect password or folder name'
    
    def unlock(self):
        return self.__unlock()

    def __run(self):
        while True:
            print('\nOptions:')
            print('1. Create Secret Folder')
            print('2. Lock Secret Folder')
            print('3. Unlock Secret Folder')
            print('4. Exit')
            choice = input('\nChoose an option: ')

            if choice == '1':
                print(self.__create())
            elif choice == '2':
                print(self.__lock())
            elif choice == '3':
                print(self.__unlock())
            elif choice == '4' or choice == "":
                break

    def run(self):
        return self.__run()


if __name__ == "__main__":
    hexbox = HexBox()
    hexbox.run()



# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ DOCUMENTATION ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #
# A secret hidden safebox for Windows to hide your contents
# Create, lock and unlock a secret folder on your computer.