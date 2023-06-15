
from datetime import datetime
import time

class TimeDisplay:
    def __init__(self):
        self.__time_format = "%H:%M:%S"

    def __display_time(self):
        while True:
            utc = datetime.utcnow()
            print(f"\rTime: {utc.strftime(self.__time_format)}", end="")
            time.sleep(1)

    def display_time(self):
        try:
            self.__display_time()
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

    def __run(self):
        self.display_time()

    def run(self):
        return self.__run()


if __name__ == "__main__":
    time_display = TimeDisplay()
    time_display.run()
