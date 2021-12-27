a = int(input())
if a <= 0:
  print('Input must be greater than 0.')
else:
  for i in range(1,a+1):
    if i%2 == 0:
      print('2'*i)
    else:
      print('5'*i)