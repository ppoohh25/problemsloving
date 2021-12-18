n = int(input())
a = []
for i in range(n):
  a.append(input())
a.sort(key = len)
for i in a:
  print(i)