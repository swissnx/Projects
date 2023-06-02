
t = int(input())

for i in range(t):
  x, y = map(int, input().split())
  xf = (x-1)//10+1  #floor num of chef's room
  yf = (y-1)//10+1  #floor num of chefina's room

  if xf <= yf:
    print(yf - xf)
  else:
    print(xf - yf)

  # 10 * (i-1) + z    i (floor) / z (room num)
  # to find i: (diff - z) / 10 + 1