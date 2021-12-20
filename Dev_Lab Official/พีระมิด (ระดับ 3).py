a = int(input())
for i in range(a):
  print('{}{}*{}'.format(' '*int(a-i-1),'*'*i,'*'*i))

for i in range(a-1):
  print('{}{}*{}'.format(' '*int(1+i),'*'*(a-2-i),'*'*(a-2-i)))