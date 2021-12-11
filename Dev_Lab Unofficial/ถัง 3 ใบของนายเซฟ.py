a = list(input())
x=[]
g = []
b = []
for i in a:
  if i == '[' or i == ']':
    pass
  else:
    x.append(i)
for i in range(len(x)):
  if x[i] == ' ':
    break
  else:
    b.append(x[i])
    
jx = ''.join(x)
sx = jx.split()
b1 = sx[0].replace('b1=','')
b2 = sx[1].replace('b2=','')
b3 = sx[2].replace('b3=','')

lb1 = b1.split(',')
lb2 = b2.split(',')
lb3 = b3.split(',')

same = list(set(lb1)&set(lb2))

for i in range(1):
  if same[i] == 'pink':
    same[i] = same[i+1]
    same[i+1] = 'pink'

if list(set(same)-set(lb3)) == []:
  print('none')
else :
  print(','.join(same))