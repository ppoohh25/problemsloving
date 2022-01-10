a = int(input())
b = []
c = []
for i in range(a*2):
  b.append(input())
for i in range(1,int(len(b)/2)+1):
  c.append(b.index(str(i)))

for i in range(len(c)):
  print('Chapter {}'.format(b[c[i]]))
  print(b[c[i]+1])