
# A program that reads a sequence of numbers and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

def odd_even():
    odd_numbers = 0
    even_numbers = 0
    print("\nOdd & Even Numbers Counter (type 0 to stop)\n")
    number = int(input("Enter a number: "))

    while number != 0:
        if number % 2 == 1:       # Check if the number is odd.
            odd_numbers += 1      # Increase the odd_numbers counter.
        else:
            even_numbers += 1                                        # Increase the even_numbers counter.
        number = int(input("\nEnter a number: "))    # Read the next number.
    return odd_numbers, even_numbers       # returns the output (without this statement we can't get/see the numbers from the function)

odd_count, even_count = odd_even()
print()
print(f"Odd numbers count:  {odd_count}")
print(f"Even numbers count: {even_count}")
