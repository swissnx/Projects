
t = int(input())
for i in range(t):
    N = int(input())
    A = list(map(int,input().split()))
    
    #sorting the array because we want to find most frequent element
    A = sorted(A)     # [1, 1, 2, 2]
    count = 1
    highest_count = 1
    i = 0  # 1 | 2 | 3
    while i<(N-1):
        if A[i] == A[i+1]: # 1==1? c=2 hc=2 | 1==2? c=1 | 2==2? c=2 hc=2
            count += 1     #Increases count whenever adjacent elements are equal
            if highest_count < count:      
                highest_count = count   #Updates the global counter

        else:   #If adjacent elements are not equal, resets count to 1
            count = 1
        i += 1
    
    print(N - highest_count)

# 3- [1, 1, 2]
# 1==1? c=2 hc=2 | 1==2? c=1 | 
# 1 | 2
