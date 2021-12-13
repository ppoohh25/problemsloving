n = input()
rn = n.replace('Number: ','')
n = int(rn)
a = []
for i in range(n):
  a.append(int(input()))
  a.sort()
  print('ROW {} : {}'.format(i+1,a))