a = []
s = ['[',']','@','#','^','%','$','*','(',')','&','!',' ',]
c = []
d = []
for i in range(3):
  a.append(input().split(':['))
for i in range(len(a)):
  if a[i][0] == 'GUITAR':
    b = list(a[i][1])
for i in range(len(b)):
  if b[i] not in s:
    c.append(b[i])
sc = ''.join(c).split(',')
if "" in sc:
  sc.remove("")
#print('GUITAR:[{}]'.format(','.join(sc)))
for i in range(len(sc)):
  if len(sc[i]) != 3:
    pass
  else:
    d.append(sc[i])
if d != []:
  d = ', '.join(d)
if d == []:
  print('GUITAR:{}'.format(d))
else:
  print('GUITAR:[{}]'.format(d))