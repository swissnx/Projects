from datetime import datetime as dt, date


def ageCalculator(year, month, day):
    today = dt.now().date()
    dob = date(year, month, day)
    age = int((today-dob).days / 365.25) # leap year is every 4 years (4 * 365 + 1 = 1461 days), 1461 / 4 = 365.25
    return age


try:
  yr = int(input("Enter year: "))
  mn = int(input("Enter month: "))
  dy = int(input("Enter day: "))
  
  age = ageCalculator(yr, mn, dy)
  
  print(f"\nAge is: {age}")
  
except ValueError as e:
  print(f"ValueError: {e}")
  
except Exception as e:
  print(f"Wrong input: {e}")
  
except:
  print("Bad input")
