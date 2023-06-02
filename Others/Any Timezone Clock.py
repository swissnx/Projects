
from datetime import datetime
import time
import pytz


class Timezone:
    def __init__(self):
        self.__time_format = "%H:%M:%S"
        self.__timezone = pytz.utc

    def __list_timezones(self):
        print("\nAvailable timezones:")
        for timezone in pytz.all_timezones:
            print(timezone)
    
    def list_timezones(self):
        return self.__list_timezones()

    def __set_timezone(self, country):
        self.__timezone = pytz.timezone(country)
    
    def set_timezone(self, country):
        return self.__set_timezone(country)

    def __display_time(self):
        while True:
            local_time = datetime.now(self.__timezone)
            print(f"\rTime: {local_time.strftime(self.__time_format)}", end="")
            time.sleep(1)

    def display_time(self):
        return self.__display_time()

    def __run(self):
        try:
            prompt = input("Print all Timezones? (y/n): ")
            if prompt.lower() == "y":
                self.__list_timezones()
                country = input("\nEnter timezone: ")
                self.__set_timezone(country)
        except Exception as e:
            print(f"Problem is: {e}")

        try:
            print()
            self.__display_time()
        except Exception as e:
            print(f"Problem is: {e}")

    def run(self):
        return self.__run()


if __name__ == "__main__":
    timezone = Timezone()
    timezone.run()
