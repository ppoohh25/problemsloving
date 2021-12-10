n = int(input())
a=[]
index = []
for i in range(n):
  a.append(int(input()))
b = int(input())
indices = [i for i, x in enumerate(a) if x == b]
if len(indices)< 3:
  print('Position: {},{}'.format(indices[0]+1,indices[1]+1))
else :
  print('Position: {},{},{}'.format(indices[0]+1,indices[1]+1,indices[2]+1))
