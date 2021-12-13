a = list(input())
b = []
c = []
vovel = ['a','e','i','o','u','A','E','I','O','U']
for i in range(len(a)):
  if a[i] in vovel:
    c.append(a[i])
    pass
  else:
    b.append(a[i])
rb = ''.join(b).replace(' ','')
rb = rb.replace('@','')
rb = rb.replace('#','')
rb = rb.replace('!','')
rb = rb.replace('.','')
rb = rb.replace(',','')
print(''.join(c))
print(rb)
