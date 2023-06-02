
t = int(input())
for i in range(t):
    N = int(input())   # festival days = holidays too // possible to fall on Sat & Sun
    A = list(map(int, input().split()))
    
    month, week = 30, 7
    workdays = (month%week) + 22   # 24 working days
    holidays = month%workdays      # 8  off days
    weeks = month//week            # 4  weeks
    
    weekends = [6, 7, 13, 14, 20, 21, 27, 28]
    
    var = list(set(A + weekends))
    
    print(len(var))
    
    # we need to know that total number of holidays in a month