n = int(input())
a = []
for i in range(n):
  a.append(int(input()))
  
a.sort(reverse = True)
for i in range(len(a)):
  print(a[i])