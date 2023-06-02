
class LeapYear:
    def __init__(self):
        pass

    def __leap_year(self, yr):
        return (yr % 4 == 0) and ((yr % 100 != 0) or (yr % 400 == 0))

    def run(self):
        print("\nCheck if the given year is a Leap or Common year")
        while True:
            year = input("\nYear (YYYY): ")
            if not year:
                break
            year = int(year)
            if year <= 0:
                break
            print("Leap year" if self.__leap_year(year) else "Common year")


if __name__ == "__main__":
    leap_year = LeapYear()
    leap_year.run()
