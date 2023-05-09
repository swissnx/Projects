
import time

def func():
    while True:
        has_high_income = int(input("Annual income: "))
        has_good_credit = int(input("Current credit score: "))

        if has_high_income >= 125000 and has_good_credit >= 950:
            print("Congrats! You are eligible for a loan.")
            time.sleep(3)
        elif has_good_credit >= 950 and has_high_income < 125000:
            print("Please contact support for further information")
            time.sleep(3)
        elif has_high_income >=125000 and has_good_credit < 950:
            print("Unfortunately, your credit score does not meet requirements")
            time.sleep(3)
        else:
            print("Unfortunately, you are not eligible for loans")
            time.sleep(3)

    has_high_income = bool(input("Annual income: "))
    has_good_credit = bool(input("Current credit score: "))

print("Please enter your financial details below, to know if you are eligible for loans.")
func()
