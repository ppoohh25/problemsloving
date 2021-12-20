a = int(input())
print('{}{}'.format(' '*int(a*3),'__'))

for i in range(a):
  print('{}__|'.format(' '*int((a-1)*3-i*3)))