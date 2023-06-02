
t = int(input())
for i in range(t):
  x, y, z = map(int, input().split())

  if x > 3:
    y1 = y*x
    y2 = ((x-1)//3)*z
    y3 = y1+y2
    print(y3)
  else:
    xf = y*x
    print(xf)