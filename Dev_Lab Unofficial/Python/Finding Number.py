n = int(input())
j =0
a = input().split()
b = int(input())
for i in range(len(a)):
  a[i] = int(a[i])
for i in range(len(a)):
  if b == a[i]:
    j+=1
if j > 0:
  print('Yes')
else:
  print('No')