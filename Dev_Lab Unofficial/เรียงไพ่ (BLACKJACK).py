a = list(map(str,input().split()))
A = 0
for i in range(len(a)):
  if a[i] == 'A':
    A = a.index('A')
    a[A]= 0
  if a[i] == 'J':
    A = a.index('J')
    a[A]= 10
  if a[i] == 'Q':
    A = a.index('Q')
    a[A]= 11
  if a[i] == 'K':
    A = a.index('K')
    a[A]= 12
for i in range(len(a)):
  a[i] = int(a[i])
a.sort()
for i in range(len(a)):
  if a[i] == 0:
    A = a.index(0)
    a[A]= 'A'
  if a[i] == 10:
    A = a.index(10)
    a[A]= 'J'
  if a[i] == 11:
    A = a.index(11)
    a[A]= 'Q'
  if a[i] == 12:
    A = a.index(12)
    a[A]= 'K'
for i in range(len(a)):
  a[i]= str(a[i])
join = ' '.join(a)
print(join)