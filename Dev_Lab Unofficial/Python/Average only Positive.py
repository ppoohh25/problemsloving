a = []
while True:
  b = float(input())
  if b < 1:
    break
  else:
     a.append(b)
average = 0
if a != [] :
  for i in range(len(a)):
    average += a[i]
if a == []:
  print('No Data')

realaver = 0
if len(a) > 0:
  realaver = average/len(a)
  print('{:.2f}'.format(realaver))