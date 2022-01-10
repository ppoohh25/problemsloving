a = list(input())
b = []
c = []
d = []
for i in range(len(a)):
  b.append(ord(a[i]))
for i in range(len(b)):
  c.append(b[i]-(i+1))
for i in range(len(c)):
  d.append(chr(c[i]))
for i in range(len(d)):
  if d[i].isupper() == True:
    d[i] = d[i].lower()
  else:
    d[i] = d[i].upper()
join = ''.join(d)
print(join)