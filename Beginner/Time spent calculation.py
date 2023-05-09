
def time_spent(hour: int, mins: int, duration: int):
    mins = mins + duration         # find a total of all minutes
    hour = hour + mins // 60       # find a number of hours hidden in minutes and update the hour
    mins = mins % 60               # correct minutes to fall in the (0..59) range
    hour = hour % 24               # correct hours to fall in the (0..23) range

    print(f"\nWill be: {hour:02}:{mins:02} o'clock")


try:
    hour = int(input("\nStarting time  (hours): "))
    mins = int(input("Starting time  (minutes): "))
    duration = int(input("Event duration (minutes): "))

except ValueError as ve:
    print(ve)

time_spent = time_spent(hour, mins, duration)
