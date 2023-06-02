
t = int(input())
for i in range(t):
    A = list(map(int, input().split()))  # 5 2 4 1 3
    n = len(A)      # 5
    
    right = 0       
    
    large = -100    # Initilise the largest value to -100. The smallest element in A is -100
    
    i = 0
    while i<n:
        # Here - we need to check if A[i] '=' large so that we can update the variable 'right'
        if A[i] >= large:   # A[i]  gives value, which is 5 in our case    
            large = A[i]
            right = i       # i   gives index, which is 0 in our case. index of 5 is 0.
        i = i + 1
    
    print(large, right)