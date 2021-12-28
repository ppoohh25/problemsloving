a = list(input())
b = []
c = []
for i in range(len(a)):
  b.append(a[i])
  c.insert(0, a[i])
  if c[0] == a[0]:
    c.pop(0)
  if i == 0:
    print('{}{}'.format(' '*int((len(a)-1)*2),b[0]))
  else:
    print('{}{} {}'.format(' '*int((len(a)-1)*2-i*2),' '.join(c),' '.join(b)))