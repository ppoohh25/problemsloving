a = list(map(int,input().split('+')))
a.sort()
for i in range(len(a)):
  a[i] = str(a[i])
join = '+'.join(a)
print(join)