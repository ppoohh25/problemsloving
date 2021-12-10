n = int(input())
a = []
for i in range(n):
  a.append(int(input()))
for i in range(len(a)):
  if a[i]%105 == 0:
    print('YES')
  else :
    print('NO')