a = list(input())
b = []
for i in range(len(a)):
  if a[i] == '[' or a[i] == ']' or a[i] == ' ':
    pass
  else:
    b.append(a[i])
realb = ''.join(b).split(',')
print(max(realb))