x = int(input())
n = int(input())
g = int(input())

steal = g-n
a = 0
for i in range(1,steal+1):
  a += i
if a > x or a > 1000:
  print('Krit was arrested')
else:
  print(x-a)