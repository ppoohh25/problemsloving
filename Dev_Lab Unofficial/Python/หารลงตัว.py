a = list(map(int,input().split(',')))
b = []
for i in range(len(a)):
  if a[i]%7 == 0  and a[i]%11 !=0 or a[i] == 1:
    b.append(str(a[i]))
join = ','.join(b)
print(join)