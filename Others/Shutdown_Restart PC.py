
import os


class ComputerPower:
    def __init__(self):
        pass

    @staticmethod
    def __shutdown_PC():
        try:
            os.system("shutdown /s /t 1")  # shuts down the pc after a delay of 1 sec.
        except Exception as e:
            print(f"Error occurred: {e}")

    @staticmethod
    def shutdown_PC():
        return ComputerPower.__shutdown_PC()

    @staticmethod
    def __restart_PC():
        try:
            os.system("shutdown /r /t 1")  # restarts the pc after a delay of 1 sec.
        except Exception as e:
            print(f"Error occurred: {e}")

    @staticmethod
    def restart_PC():
        return ComputerPower.__restart_PC()

    @staticmethod
    def __run():
        answer = input("Do you want to shut down or restart your computer? (shutdown/restart): ")

        if answer.lower() == 'shutdown':
            answer = input("Sure to shut down your computer? (y/n): ")
            if answer.lower() == 'y':
                ComputerPower.__shutdown_PC()

        elif answer.lower() == 'restart':
            answer = input("Sure to restart your computer? (y/n): ")
            if answer.lower() == 'y':
                ComputerPower.__restart_PC()

    def run(self):
        return self.__run()


if __name__ == "__main__":
    pc_power = ComputerPower()
    pc_power.run()
