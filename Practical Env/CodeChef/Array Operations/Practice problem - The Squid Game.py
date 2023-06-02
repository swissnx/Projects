
t = int(input())
for i in range(t):
    n = int(input())    # number of players
    a = list(map(int,input().split()))   # amount of money added to the prize pool
    
    lst = sum(a)
    prize = lst - min(a)
    
    print(prize)