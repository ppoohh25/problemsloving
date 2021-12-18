a = []
while True:
  i = int(input())
  if i == 0:
    break
  else:
    a.append(i)
a.sort()
if a == []:
  print('Total : 0')
  print('Maximum : 0')
  print('Minimum : 0')
else:
  print('Total : {}'.format(len(a)))
  print('Maximum : {}'.format(max(a)))
  print('Minimum : {}'.format(min(a)))