
from datetime import datetime
import time
import pytz

# def timezone_generator():     # if we'd like to use generator
#     for timezone in pytz.all_timezones:
#         yield timezone

time_format = "%H:%M:%S"
timezone = pytz.utc

try:
    prompt = input("Print all Timezones? (y/n): ")

    if prompt.lower() == "y":
        print("\nAvailable timezones:")
        for timezone in pytz.all_timezones:  #if we use generator then:  for timezone in timezone_generator():
            print(timezone)
        country = input("\nEnter timezone: ")
        timezone = pytz.timezone(country)

except Exception as e:
    print(f"Problem is: {e}")

try:
    print()
    while True:
        local_time = datetime.now(timezone)
        print(f"\rTime: {local_time.strftime(time_format)}", end="")
        time.sleep(1)

except Exception as e:
    print(f"Problem is: {e}")
