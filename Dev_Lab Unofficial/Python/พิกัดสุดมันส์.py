point = list(input())
point.pop(0)
point.pop(len(point)-1)
p = ''.join(point).split(',')
x = int(p[0])
y = int(p[1])
row = int(input())

if x > row or y > row or x < 0 or y < 0 or y == row:
  print('That position is not loaded.')

elif x < row and y < row:
  for i in range(row-y-1):
    print('#'*row)
  
  print('{}*{}'.format('#'*int(x),'#'*int(row-x-1)))

  for i in range(y):
    print('#'*row)