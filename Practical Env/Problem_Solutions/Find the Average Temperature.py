
def monthly_aver_room_temp():
    temps = [[0.0 for h in range(24)] for d in range(31)]
    for d in range(31):
        for h in range(24):
            while True:
                try:
                    temp = float(input(f"Enter temperature for day {d+1}, hour {h}: "))
                    temps[d][h] = temp
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid temperature.")
    total = 0.0

    for day in temps:
        total += day[11]

    average = total / 31
    print("Average temperature at noon:", average)

monthly_aver_room_temp()


def highest_temp_in_month():
    temps = [[0.0 for h in range(24)] for d in range(31)]
    for d in range(31):
        for h in range(24):
            while True:
                try:
                    temp = float(input(f"Enter temperature for day {d+1}, hour {h}: "))
                    temps[d][h] = temp
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid temperature.")
    highest = -100.0

    for day in temps:
        for temp in day:
            if temp > highest:
                highest = temp

    print("The highest temperature was:", highest)

highest_temp_in_month()


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def monthly_aver_room_temp():
  temps = [[0.0 for h in range(24)] for d in range(31)]
  # The matrix is magically updated here.
  total = 0.0

  for day in temps:
      total += day[11]

  average = total / 31
  print("Average temperature at noon:", average)

monthly_aver_room_temp()


def highest_temp_in_month():
  temps = [[0.0 for h in range(24)] for d in range(31)]
  # The matrix is magically updated here.
  highest = -100.0
  
  for day in temps:
      for temp in day:
          if temp > highest:
              highest = temp
  
  print("The highest temperature was:", highest)

highest_temp_in_month()

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Temperature conversion
def fah_cel(degree):
  return (degree-32) * (5/9)


usr = int(input("\nin Fahrenheit: "))
print(f"in Celcius: {fah_cel(usr)}°")

def cel_fah(degree):
  return ((9/5) * degree) + 32

usr = int(input("\n\nin Celcius: "))
print(f"in Fahrenheit: {cel_fah(usr)}")


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

