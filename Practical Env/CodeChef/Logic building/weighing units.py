
t = int(input())
for i in range(t):
  w, x, y, z = map(int, input().split())
  if ((x+y)==w) or ((x+z)==w) or ((y+z)==w) or (w in [x, y, z]) or ((x+y+z)==w):
    print("yes")
  else:
    print("no")