
class IsAHappyNumber:
    def __init__(self):
        self.__number = input("Number: ")

    def __is_happy(self, n):
        seen = set()
        while n not in seen:
            seen.add(n)
            n = _sum(int(i) ** 2 for i in str(n))
        return n == 1

    def __run(self):
        while True:
            if self.__number == "":
                break
            self.__number = int(self.__number)
            if self.__is_happy(self.__number):
                print(f"\n{self.__number} is a happy number")
            else:
                print(f"\n{self.__number} is not a happy number")
            self.__number = input("\nNumber: ")
    
    def run(self):
        try:
            self.__run()

        except Exception as e:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")


if __name__ == "__main__":
    h_num = IsAHappyNumber()
    h_num.run()





# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ DOCUMENTATION ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #

def isHappyNumber(num):
    rem = _sum = 0

    while num > 0:
        rem = num%10
        _sum = _sum + (rem*rem) #4
        num = num//10 #8
    return _sum #4

num = 82
result = num

while result != 1 and result != 4:
    result = isHappyNumber(result)


if result == 1:
    print(str(num) + " is a happy number")

elif result == 4:
    print(str(num) + " is not a happy number")


""" num is set to 82 and result is set to num, so result is also 82.
The while loop condition is checked. Since result is not equal to 1 or 4, the loop is entered.
The isHappyNumber function is called with result (82) as an argument.
Inside the function, rem and _sum are initialized to 0.
The inner while loop condition is checked. Since num (82) is greater than 0, the loop is entered.
rem is set to the last digit of num (82 % 10 = 2).
The square of rem (2 * 2 = 4) is added to _sum, so _sum becomes 4.
The last digit is removed from num by performing integer division by 10 (82 // 10 = 8).
The inner while loop condition is checked again. Since num (8) is still greater than 0, the loop continues.
rem is set to the last digit of num (8 % 10 = 8).
The square of rem (8 * 8 = 64) is added to _sum, so _sum becomes 68.
The last digit is removed from num by performing integer division by 10 (8 // 10 = 0).
The inner while loop condition is checked again. Since num (0) is not greater than 0, the loop exits.
The function returns the final value of _sum, which is 68.
The return value of the function (68) is assigned to result.
The outer while loop condition is checked again. Since result (68) is not equal to 1 or 4, the loop continues and steps 3-15 are repeated with the new value of result.
This process continues until eventually, after several iterations, result becomes equal to 1 and the outer loop exits.
The final value of result (1) indicates that the original number (82) was a happy number. """

