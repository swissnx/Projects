

t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    a = 500
    b = 1000
    a2b = (a - (x*2)) + (b - ((x+y)*4))

    b2a = (b - (y*4)) + (a - ((y+x)*2))

    if a2b == b2a or a2b > b2a:
        print(a2b)
    else:
        print(b2a)

