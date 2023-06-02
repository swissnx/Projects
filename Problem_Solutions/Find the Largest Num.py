
# Sample_1
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

largest_number = max(number1, number2, number3)   #the same works with min()

print("The largest number is:", largest_number)



# Sample_2
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

largest_number = number1         # We temporarily assume that the first number is the largest one. We will verify this soon.

if number2 > largest_number:     # We check if the second number is larger than current largest_number and update largest_number if needed.
    largest_number = number2

if number3 > largest_number:     # We check if the third number is larger than current largest_number and update largest_number if needed.
    largest_number = number3

print("The largest number is:", largest_number)



# Sample_3
largest_number = -99999999
counter = 0

while True:
    number = int(input("Enter a number or type -1 to end program: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")



# Sample_4
largest_number = -99999999
counter = 0

number = int(input("Enter a number or type -1 to end program: "))

while number != -1:                                                                # pay attention to the same spot on 'break' program
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Enter a number or type -1 to end program: "))

if counter:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")



# Sample_5
def three_numbers():
    num1 = float(input("> "))
    num2 = float(input("> "))
    num3 = float(input("> "))

    if num2 <= 10:
        print(f"{num2} is less than {num1}")
    elif num3 <= num2 or num1 >= num2:
        if num3 <= num2:
            print(f"{num3} is less than {num2}")
        else:
            print(f"{num1} wins the race")
    else:
        print(f"{num3} is greater than both {num1} and {num2}")

print("\nCompare the three Numbers\n")
three_numbers()



# Sample_6
testArr = [11, 22, 33, 22, 11] 
result = testArr[0] 
for iter in testArr:
    if iter > result:
        result = iter
print(result)