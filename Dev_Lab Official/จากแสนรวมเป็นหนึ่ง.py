a = list(map(int,input()))
b = 0
c = 0
d = 0
for i in range(len(a)):
  b +=a[i]
x = [int(i) for i in str(b)]
for i in range(len(x)):
  c +=x[i]
y = [int(i) for i in str(c)]
for i in range(len(y)):
  d+=y[i]
print(d)