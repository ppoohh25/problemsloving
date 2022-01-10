a = list(input())
a.pop(0)
a.pop(len(a)-1)
b = ''.join(a).split(', ')
count = 0
for i in range(len(b)):
  for j in range(len(b)):
    if b[i] == b[j]:
      count += 1
if count > len(b):
  print('True')
else:
  print('False')