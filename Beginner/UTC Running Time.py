
from datetime import datetime
import time

time_format = "%H:%M:%S"

while True:
    utc = datetime.utcnow()
    print(f"\rTime: {utc.strftime(time_format)}", end="")
    time.sleep(1)
