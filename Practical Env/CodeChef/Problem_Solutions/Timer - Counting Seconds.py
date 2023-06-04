
# We need a class able to count seconds.
# Read them carefully as the class you're about write will be used to launch rockets carrying international missions to Mars.
# It's a great responsibility. We're counting on you!

# Your class will be called "Timer". Its constructor accepts three arguments representing *hours* (a value from range [0..23] -
# we will be using the military time), *minutes* (from range [0..59]) and *seconds* (from range [0..59]).

# Zero is the default value for all of the above parameters. There is no need to perform any validation checks.

# The class itself should provide the following facilities:
#    • objects of the class should be "printable", i.e. they should be able to implicitly convert themselves into strings of the following form: "hh:mm:ss",
#      with leading zeros added when any of the values is less than 10;
#    • the class should be equipped with parameterless methods called 'next_second()' and 'previous_second()', incrementing the time stored inside objects
#      by +1/-1 second respectively.

# Use the following hints:
#    • all object's properties should be private;
#    • consider writing a separate function (not method!) to format the time string.

def two_digits(val):
    s = str(val)
    if len(s) == 1:
        s = '0' + s
    return s


class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        return two_digits(self.__hours) + ":" + \
               two_digits(self.__minutes) + ":" + \
               two_digits(self.__seconds)

    def next_second(self):
        self.__seconds += 1
        if self.__seconds > 59:
            self.__seconds = 0
            self.__minutes += 1
            if self.__minutes > 59:
                self.__minutes = 0
                self.__hours += 1
                if self.__hours > 23:
                    self.__hours = 0

    def prev_second(self):
        self.__seconds -= 1
        if self.__seconds < 0:
            self.__seconds = 59
            self.__minutes -= 1
            if self.__minutes < 0:
                self.__minutes = 59
                self.__hours -= 1
                if self.__hours < 0:
                    self.__hours = 23




try:  # this code block should be carefully checked and fixed
  x = int(input("\nHours   in [00] format: "))
  y = int(input("Minutes in [00] format: "))
  z = int(input("Seconds in [00] format: "))
  if len(x) != 2 or len(y) != 2 or len(z) != 2:
    print("Wrong input. Try again :(")
except:
  print("oops")


timer = Timer(x, y, z)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
