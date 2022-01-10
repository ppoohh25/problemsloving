a = []
b = []
c = ['st','nd','rd','th','th']
while True:
  i = input()
  if i != '-':
    a.append(int(i))
  else:
    break
for i in a:
  b.append(str(i)+c[i-1])
if a[0] == 0:
  print('Error! Not have this floor')
elif a[0] != 0:
  print('OK! Wait please')
  print('---------------')
  print('Lift is arriving!')
  print('---------------')
  for i in range(len(b)):
    if b[i] != max(b):
      print('Lift is going up!')
      print('---------------')
      print('Lift has reached the {} floor!'.format(b[i]))
      print('---------------')
    else:
      print('Lift is going up!')
      print('---------------')
      print('Lift has reached the {} floor!'.format(b[i]))
