
import os

def shutdown_PC():
    try:
        os.system("shutdown /s /t 1")  # shuts down the pc after a delay of 1 sec.
    except Exception as e:
        print(f"Error occured: {e}")

if __name__ == "__main__":
    answer = input("Sure to shut down your computer? (y/n): ")
    if answer.lower() == 'y':
        shutdown_PC()
