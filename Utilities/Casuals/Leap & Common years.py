
class LeapYear:
	def __init__(self):
		pass

	def __leap_year(self, yr):
		return (yr % 4 == 0) and ((yr % 100 != 0) or (yr % 400 == 0))

	def run(self):
		print("\nCheck if the given year is - Leap or Common year")

		while True:
			try:
				year = input("\nYear (YYYY): ")
			
				if not year:
					break
			
				year = int(year)
				if year <= 0:
					break
			
				print("Leap year" if self.__leap_year(year) else "Common year")
			
			except Exception as e:
				return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"


if __name__ == "__main__":
    leap_year = LeapYear()
    leap_year.run()




""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# this line of code is for a comparison with a first one!
def leap_year(year):
	if (year % 4) == 0:
		if (year % 100) == 0:
			if (year % 400) == 0:
				return True
			else:
				return False
		else:
			return True
	else:
		return False

print("\nCheck if the given year is a Leap or Common year")
while True:
  user = input("\nEnter a year: ")
  if user == "":
    print("\nFinished.")
    break
  user = int(user)
  if user <= 0:
    print("\nFinished.")
    break
  if leap_year(user):
    print("Leap year")
  else:
    print("Common year")


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Simple and small:
def func(yr):
	if (yr % 4 == 0) and ((yr % 100 != 0) or (yr % 400 == 0)):
		print("Leap year")
	else:
		print("Common year")

year = int(input("\nEnter a year: "))
func(year)


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# calendar Library implementation
import calendar

year = calendar.isleap(int(input("Enter a year: ")))
print(year)


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# # # ------------------------- EDUCATIONAL FROM PYTHON INSTITUTE ------------------------- # # #


def is_year_leap(year):
	if year % 4 != 0:   # 0=0 true, 0!=0 false (0 is not equal to 0, is false, because they are equal)
		return False
	elif year % 100 != 0:
		return True
	elif year % 400 != 0:
		return False
	else:
		return True


# This implementation of the is_year_leap function is mostly correct, but there's an error in the conditions in the elif statements.
# If a year is divisible by 4 and not divisible by 100, it is a leap year. However, if a year is divisible by both 100 and 400, it is still a leap year.
# So, the code should look like this:
def is_year_leap(year):
	if year % 4 != 0:   # 0=0 true, 0!=0 false (0 is not equal to 0, is false, because they are equal)
		return False
	elif year % 100 == 0 and year % 400 != 0:
		return False
	else:
		return True


#####################################################################################################################

def is_year_leap(year):
	if year % 4 != 0:   # 0=0 true, 0!=0 false (0 is not equal to 0, is false, because they are equal)
		return False
	elif year % 100 != 0:
		return True
	elif year % 400 != 0:
		return False
	else:
		return True

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(f"{yr} -> ",end=" ")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")


""" The code tests the is_year_leap function with a set of test data:
test_data = [1900, 2000, 2016, 1987]

and expected results:
test_results = [False, True, True, False].

For each year in the test data, the year is assigned to the variable yr
and passed as an argument to the is_year_leap function. The result of the function call is assigned to the variable result.

Next, a comparison is made between the result of the function and the expected result, stored in test_results[i].
If the result and expected result match, the code outputs "OK". If they don't match, the code outputs "Failed". """



#####################################################################################################################

def is_year_leap(year):
	if year % 4 != 0:
		return False
	elif year % 100 != 0:
		return True
	elif year % 400 != 0:
		return False
	else:
		return True

def days_in_month(year,month):
	if year < 1582 or month < 1 or month > 12:
		return None
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	res  = days[month - 1]
	if month == 2 and is_year_leap(year):
		res = 29
	return res

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr,mo,"-> ",end=" ")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")



#####################################################################################################################

def is_year_leap(year):
	if year % 4 != 0:
		return False
	elif year % 100 != 0:
		return True
	elif year % 400 != 0:
		return False
	else:
		return True

def days_in_month(year, month):
	if year < 1582 or month < 1 or month > 12:
		return None
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	res  = days[month - 1]
	if month == 2 and is_year_leap(year):
		res = 29
	return res

def day_of_year(year, month, day):
	days = 0
	for m in range(1, month):
		md = days_in_month(year, m)
		if md == None:
			return None
		days += md
	md = days_in_month(year, month)
	if day >= 1 and day <= md:
		return days + day
	else:
		return None

print(day_of_year(2000, 12, 31))



""" The day_of_year function takes three arguments, year, month, and day, and returns the day of the year for a given date.

Here's how the code works:

1. The function starts by initializing a variable days to 0.
2. The code then uses a for loop to iterate over all the months from 1 to the input month month.
3. For each iteration, it calls the days_in_month function to get the number of days in the current month, and assigns the result to the variable md.
4. If md is None, the function returns None, indicating that the year or month is not valid.
5. If the current month is valid, the code adds the number of days to the running total stored in the days variable.
6. After the loop, the function calls days_in_month again, passing in the year and the input month month, and assigns the result to md.
7. The function then checks if the input day day is between 1 and md, inclusive.
8. If the day is valid, the function returns days + day, which is the sum of the total number of days from all the previous months and the input day.
9. If the day is not valid, the function returns None.

The code then calls the day_of_year function, passing in the year 2000, month 12, and day 31, and prints the result, which is 365 in this case.



Let's say the input to the function is year = 2000, month = 12, day = 31.

1. The variable "days" is initialized to 0.
2. The "for" loop iterates over the range of integers from 1 to (month-1), in this case 1 to 11.
    a. In each iteration of the loop, the function "days_in_month" is called with the current year and month (m).
    b. The returned value is stored in the variable "md".
    c. If "md" is None, the function returns None.
    d. If "md" is not None, the value of "md" is added to the variable "days".
3. After the for loop, the function "days_in_month" is called again, this time with the year and the actual month (12 in this case).
    The returned value is stored in the variable "md".
4. Finally, if the input day is greater than or equal to 1 and less than or equal to "md", the function returns the value of "days + day".
    If the input day is outside this range, the function returns None.

So, in this case, the function will return the value of (0 + 31) = 31,
as the input day is 31, which is within the range of valid days for the month of December. """



""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

