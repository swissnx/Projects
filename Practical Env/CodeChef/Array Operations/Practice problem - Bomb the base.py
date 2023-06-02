
# NOT FINISHED YET

t = int(input())
for i in range(t):
    n, x= map(int, input().split())
    a = list(map(int, input().split()))
    
    # n = house nums in range(1, n)
    # x = bomb attack strength
    # a = defence system strength
    
    # find the number of houses that can get destroyed if the bomb can hit any houses
    
    target_houses = 0
    i = 0
    
    while i < n:
        if a[i] < x:
            target_houses = i + 1
        i += 1
    
    print(target_houses)