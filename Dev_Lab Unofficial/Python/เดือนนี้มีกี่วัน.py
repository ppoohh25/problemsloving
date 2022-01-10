a = input().split()
a[1] = int(a[1])-543

if a[0] == '2' and (a[1]%4 ==0 and a[1]%100 != 0):
  print(29)
elif a[0] == '2':
  print(28)
if a[0] == '10':
  print(31)
if a[0] == '4':
  print(30)