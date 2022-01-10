a = list(map(int,input().split()))
row = a[0]
cut = a[1]

for i in range(cut):
  print('{}{}{}'.format('-'*int(cut-i),'*'*int(row-2*(cut-i)),'-'*int(cut-i)))
for i in range(row-cut*2):
  print('*'*row)
for i in range(cut):
  print('{}{}{}'.format('-'*int(cut-(cut-1)+i),'*'*int(row-2*(cut-(cut-1)+i)),'-'*int(cut-(cut-1)+i)))