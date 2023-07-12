
import os


class ComputerPower:
    def __init__(self):
        pass

    @staticmethod
    def __shutdown_PC():
        try:
            os.system("shutdown /s /t 1")  # shuts down the pc after a delay of 1 sec.

        except Exception as e:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")

    @staticmethod
    def shutdown_PC():
        return ComputerPower.__shutdown_PC()

    @staticmethod
    def __restart_PC():
        try:
            os.system("shutdown /r /t 1")  # restarts the pc after a delay of 1 sec.

        except Exception as e:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")

    @staticmethod
    def restart_PC():
        return ComputerPower.__restart_PC()

    @staticmethod
    def run():
        try:
            print("Do you want to shut down or restart your computer?")
            answer = input("\n1. Shutdown\n2. Restart\n\nChoice: ")

            if answer == '1':
                conf = input("Sure to shut down your computer? (y/n): ")
                if conf.lower() == 'y':
                    ComputerPower.__shutdown_PC()

            elif answer == '2':
                conf = input("Sure to restart your computer? (y/n): ")
                if conf.lower() == 'y':
                    ComputerPower.__restart_PC()

        except Exception as e:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")


if __name__ == "__main__":
    pc_power = ComputerPower()
    pc_power.run()
