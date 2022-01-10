a = list(input())
b = 0
for i in range(len(a)):
  if a[i] == ';':
    b += 1
print(b)