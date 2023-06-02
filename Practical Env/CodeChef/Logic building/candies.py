
t = int(input())
for i in range(t):
  n, m = map(int, input().split())
  if n%m == 0 and (n//m)%2 == 0:
    print('yes')
  else:
    print('no')