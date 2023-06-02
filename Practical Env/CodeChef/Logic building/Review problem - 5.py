
# Solution 1:
t = int(input())
for i in range(t):
    p = int(input())

# score = total score of the participant
# problems = 10
# invalid score = -1
# score of each prob = 1 or 100

    if p % 10 > 10 or p % 100 > 10:
        print(-1)
    
    elif p >= 0 and p <= 10:
        print(p)
    
    elif p >= 100 and p <= 1000:
        x = (p % 100) + (p // 100)
        print(x)



# Solution 2:
t = int(input())
for i in range(t):
    P = int(input())

    if ((P//100 + P%100) <= 10):
        print((P//100 + P%100))
    else:
        print(-1)

