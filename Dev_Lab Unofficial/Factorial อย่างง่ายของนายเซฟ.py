a = input()
b = []
for i in a:
  if i == '[' or i == ']':
    pass
  else :
    b.append(i)
join = ''.join(b)
#print('{}!:{}'.format(b,c))
intj = int(join)
fac = 1
for i in range(1, intj+1):
  fac = fac*i
print('{}!:{}'.format(intj,fac))