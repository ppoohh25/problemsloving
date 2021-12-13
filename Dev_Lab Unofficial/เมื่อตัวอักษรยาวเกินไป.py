name = list(input())
n = int(input())
a = []
if len(name)> n and n != 22 and n != 0:
    name[n+1] = '...'
    for i in range(n+2):
      a.append(name[i])
if len(name) == n:
  print(''.join(name))
if n ==0 :
  print('...')
if n == 22:
  name[n] = '...'
  for i in range(n+1):
    a.append(name[i])
  print(''.join(a))

else:
  print(''.join(a).replace(' ',''))