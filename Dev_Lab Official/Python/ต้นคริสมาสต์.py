a = int(input())

for i in range(a):
  for j in range(i+2):
    print('{}{}*{}'.format(' '*int(a-j),'*'*j,'*'*j))
print('{}|'.format(' '*a))
print('{}V{}'.format('='*a,'='*a))