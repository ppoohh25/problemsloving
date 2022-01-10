n = int(input())
a = 0
b = []
for i in range(n):
  b.append(int(input()))
for i in range(len(b)):
  a += b[i]
print('{} THB'.format(a))
