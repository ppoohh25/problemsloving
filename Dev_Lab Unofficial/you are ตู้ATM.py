a = int(input())
b = 0
c = 0
d = 0
if a >= 1000:
  b = a//1000
  a -= 1000*b
  print('1000 * {}'.format(b))
else :
  print('1000 * 0')
if a >= 500:
  c = a//500
  a -= 500*c
  print('500 * {}'.format(c))
else :
  print('500 * 0')
if a >= 100:
  d = a//100
  a -= 100*d
  print('100 * {}'.format(d))
else:
  print('100 * 0')