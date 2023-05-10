
import os

def shutdown_PC():
    try:
        os.system("shutdown /s /t 1")  # shuts down the pc after a delay of 1 sec.
    except Exception as e:
        print(f"Error occurred: {e}")

def restart_PC():
    try:
        os.system("shutdown /r /t 1")  # restarts the pc after a delay of 1 sec.
    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    answer = input("Do you want to shut down or restart your computer? (shutdown/restart): ")

    if answer.lower() == 'shutdown':
        answer = input("Sure to shut down your computer? (y/n): ")
        if answer.lower() == 'y':
            shutdown_PC()

    elif answer.lower() == 'restart':
        answer = input("Sure to restart your computer? (y/n): ")
        if answer.lower() == 'y':
            restart_PC()
