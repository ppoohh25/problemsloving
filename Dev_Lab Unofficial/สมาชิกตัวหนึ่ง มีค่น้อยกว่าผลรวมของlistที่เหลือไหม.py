a = list(input())
a.pop(0)
a.pop(len(a)-1)
t = 0
b = ''.join(a).split(',')
for i in range(len(b)):
  b[i] = int(b[i])
for i in range(len(b)):
  if b[i] < sum(b)-b[i]:
    t +=1
if t == len(b):
  print('true')
else:
  print('false')