a = list(input())
for i in range(len(a)):
  if i%2 !=0:
    a[i]= a[i].upper()
join = ''.join(a)
print(join)