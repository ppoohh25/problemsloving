n = int(input())
a = []
for i in range(n):
  a.append(int(input()))
  
b = a[::-1]
for i in range(n):
  print(b[i])