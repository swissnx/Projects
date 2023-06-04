
class TimeSpent:
    def __init__(self):
        self.__hour = 0
        self.__mins = 0
        self.__duration = 0

    def __calculate_time_spent(self):
        mins = self.__mins + self.__duration     # find a total of all minutes
        hour = self.__hour + mins // 60          # find a number of hours hidden in minutes and update the hour
        mins = mins % 60                         # correct minutes to fall in the (0..59) range
        hour = hour % 24                         # correct hours to fall in the (0..23) range

        print(f"\nWill be: {hour:02}:{mins:02} o'clock")

    def __run(self):
        try:
            self.__hour = int(input("\nStarting time (hours): "))
            self.__mins = int(input("Starting time (minutes): "))
            self.__duration = int(input("Event duration (minutes): "))

        except ValueError as ve:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{ve}\u001b[0m")
        self.__calculate_time_spent()

    def run(self):
        return self.__run()


if __name__ == "__main__":
    time_spent = TimeSpent()
    time_spent.run()
