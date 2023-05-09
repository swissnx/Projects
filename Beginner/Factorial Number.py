
# 0! = 1
# 1! = 1
# 2! = 1 * 2
# 3! = 1 * 2 * 3
# 4! = 1 * 2 * 3 * 4
# :
# :
# n! = 1 * 2 * 3 * 4 * ... * n-1 * n
# n! = n * (n-1) * (n-2) * ... * 3 * 2 * 1

import sys

sys.set_int_max_str_digits(0)

def factorial(num):
  if num <= 0:
    return None
  if num < 2:
    return 1

  fact = 1
  for i in range(2, num + 1):
    fact *= i
  return fact


start = int(input("Starting point: "))
end = int(input("Ending point:   "))
print()

for num in range(start, end):
  print(f"{num} - {factorial(num)}")
