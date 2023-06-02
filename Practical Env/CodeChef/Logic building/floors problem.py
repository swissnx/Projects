
t = int(input())
for i in range(t):
    a, b, x, y = map(int,input().split())
    # if (v:=(a%x = 0)) == (p:=(b%y == 0)):
    #     print("both")
    z = a/x
    v = b/y
    if z == v:
      print("both")
    elif z < v:
      print("chef")
    else:
      print("chefina")