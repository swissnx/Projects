
t = int(input())
for i in range(t):
  n, x, p = map(int, input().split())

  #equation for calculating chef's score
  score = x*3 + (-1)*(n-x)

  #check conditions for chef's score
  if score >= p:
    print("Pass")
  else:
    print("Fail")