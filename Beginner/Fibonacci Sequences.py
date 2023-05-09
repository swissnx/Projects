
import sys

sys.set_int_max_str_digits(0)

def fibonacci(num):
  if num < 1:
    return None
  if num < 3:
    return 1

  elem1 = elem2 = 1
  total = 0
  for i in range(3, num + 1):
    total = elem1 + elem2
    elem1, elem2 = elem2, total
  return total

start = int(input("Starting point: "))
end = int(input("Ending point:   "))
print()

for num in range(start, end):
  print(f"{num} - {fibonacci(num)}")
print()
