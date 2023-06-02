
t = int(input())
for i in range(t):
    A = list(map(int,input().split()))  # [5, 2, 4, 1, 3]
    N = len(A)   # 5
    
    
    minElement = A[0]  # A[0]=5 | A[1]=2 | A[3]=1
    minElementIndex = 0  # 1 | 3
    i = 1  # starting from 1 cos 0 is taken as 5 as min num | 2 -> 3 | 4 -> 5
    while i < N:  # A[i]=2 < 5(lst len) valid | A[3]=1<5(lst len) | 
        if A[i] < minElement:
            minElement = A[i]
            minElementIndex = i
        i += 1
    
    
    i = minElementIndex   # 5 = 3
    while i > 0:
        A[i],A[i-1] = A[i-1], A[i]
        i -= 1
    
    print(*A)

