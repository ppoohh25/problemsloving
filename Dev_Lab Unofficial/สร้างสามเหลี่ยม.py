a = int(input())
for i in range(a-1):
  print('{}/{}\\'.format(' '*(a-i-1),' '*i*2))
print('/{}\\'.format('_'*(a*2-2)))