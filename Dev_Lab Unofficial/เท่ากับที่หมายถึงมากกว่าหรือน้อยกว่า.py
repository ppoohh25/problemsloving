a = list(input())
b = ''.join(a).split('==')
for i in range(len(b)):
  b[i] = int(b[i])
if b[0] > b[1]:
  print(b[0])
else:
  print(b[1])