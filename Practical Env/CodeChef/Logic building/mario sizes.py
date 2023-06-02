
t = int(input())
for i in range(t):
  x = int(input())
  if x%3 == 0:
    print('Normal')
  elif (x-1)%3 == 0:
    print("Huge")
  else:
    print("Small")