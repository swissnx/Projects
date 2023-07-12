
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

        return f"\nWill be: {hour:02}:{mins:02} o'clock"

    def __run(self):
        try:
            self.__hour = int(input("\nStarting time (hours): "))
            self.__mins = int(input("Starting time (minutes): "))
            self.__duration = int(input("Event duration (minutes): "))

            print(self.__calculate_time_spent())

        except ValueError as ve:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{ve}\033[0m"

        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def run(self):
        return self.__run()


if __name__ == "__main__":
    time_spent = TimeSpent()
    time_spent.run()
