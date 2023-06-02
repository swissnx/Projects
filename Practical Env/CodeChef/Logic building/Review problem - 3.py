
# Review problem - 3
t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    income = 2**x
    spent = income // 2
    for i in range(2, n+1):
        spent += (income - spent) // 2
    saved = income - spent
    print(saved)


