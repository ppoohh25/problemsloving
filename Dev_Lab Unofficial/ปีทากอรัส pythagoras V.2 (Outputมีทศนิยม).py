import math
a = float(input())
b = float(input())
a2 = a**2
b2 = b**2
c = a2+b2
rc = math.sqrt(c)
if rc%1 ==0:
  print(int(rc))
else :
  print('{:.2f}'.format(rc))