a = list(map(str,input().split()))
a1 = int(a[0])
opp = a[1]
a2 = int(a[2])
join = ' '.join(a)
for i in range(len(a)):
  if a[i] == '-':
    print(join,'= {}'.format(a1 - a2))
  if a[i] == '+':
    print(join,'= {}'.format(a1 + a2))
  if a[i] == '*':
    print(join,'= {}'.format(a1 * a2))
  if a[i] == '/':
    print(join,'= {}'.format(a1 / a2))