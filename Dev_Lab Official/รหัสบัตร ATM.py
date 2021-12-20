a = list(input())
num = ['1','2','3','4','5','6','7','8','9','0']
b = []
for i in range(len(a)):
  if a[i] not in num:
    a[i] = '.'
c = ''.join(a).split('.')

for i in range(len(c)):
  if c[i] == "":
    pass
  else:
    b.append(c[i])
for i in range(len(b)):
  b[i] = int(b[i])
if sum(b) < 100:
  print('00{}'.format(sum(b)))
else:
  print(sum(b))