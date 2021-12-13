a = int(input())
b = 0
for i in range(1,13):
  print('{} x {} = {}'.format(a,i,a*i))
  b+= a*i
c ='{:,}'.format(b)
print('รวม : {}'.format(c+'.00'))