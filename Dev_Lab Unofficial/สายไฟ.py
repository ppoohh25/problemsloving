a = []
b = 0
color = ['Red','Yellow','Blue','White']
for i in range(3):
  i = input()
  a.append(i)
  if i == 'Blue':
    b += 1
if a[0] not in color:
  print('ERROR')
elif 'Red' not in a:
  print('Second Line')
elif a[2] == 'White':
  print('Third Line')
elif 1 < b < 3:
  print('First Line')
else:
  print('Third Line')