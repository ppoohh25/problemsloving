a = int(input())
b = 0
c = 0
if a >= 5:
  b = a//5
  a -= 5*b
  c += b
  b = 0
if a >= 4:
  b = a//4
  a -= 4*b
  c += b
  b = 0
if a >= 3:
  b = a//3
  a -= 3*b
  c += b
  b = 0
if a >= 2:
  b = a//2
  a -= 2*b
  c += b
  b = 0
if a >= 1:
  b = a//1
  a -= 1*b
  c += b
  b = 0
print(c)