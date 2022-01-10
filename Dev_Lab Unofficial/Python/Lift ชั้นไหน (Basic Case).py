a = int(input())
b = [1,2,3,4,5]
c = ['st','nd','rd','th','th']
if a in b:
  print('OK! Wait please')
  print('---------------')
  print('Lift is arriving!')
  print('---------------')
  print('Lift is going up!')
  print('---------------')
  print('Lift has reached the {}{} floor!'.format(b.index(a)+1,c[a-1]))
else:
  print('Error! Not have this floor')