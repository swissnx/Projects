
class ZodiacSigns:
    def __init__(self):
        self.__zodiac_signs = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
        self.__year_signs = ['Monkey', 'Rooster', 'Dog', 'Pig', 'Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Sheep']
    
    def __get_zodiac_sign(self, month, day):
        if (month == 1 and day >= 20) or (month == 2 and day <= 18):
            return self.__zodiac_signs[10]
        elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
            return self.__zodiac_signs[11]
        elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
            return self.__zodiac_signs[0]
        elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
            return self.__zodiac_signs[1]
        elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
            return self.__zodiac_signs[2]
        elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
            return self.__zodiac_signs[3]
        elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
            return self.__zodiac_signs[4]
        elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
            return self.__zodiac_signs[5]
        elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
            return self.__zodiac_signs[6]
        elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
            return self.__zodiac_signs[7]
        elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
            return self.__zodiac_signs[8]
        else:
            return self.__zodiac_signs[9]

    def __get_year_sign(self, year):
        return self.__year_signs[year % 12]

    def run(self):
        while True:
            try:
                month = int(input("Birth month: "))
                day = int(input("Birth day: "))
                year = int(input("Birth year: "))

                zodiac_sign = self.__get_zodiac_sign(month,day)
                year_sign = self.__get_year_sign(year)

                print(f"\nZodiac sign is {zodiac_sign}")
                print(f"Year sign is {year_sign}")

            except Exception as e:
                print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")


if __name__ == "__main__":
    zodiac = ZodiacSigns()
    zodiac.run()
