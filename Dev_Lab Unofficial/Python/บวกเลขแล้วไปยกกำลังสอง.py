a = list(input())
b = list(input())
num = ['1','2','3','4','5','6','7','8','9',]
if a[0] not in num or b[0] not in num:
  print('Error')
else:
  bint = int(''.join(b))
  aint = int(''.join(a))
  print('{:,}'.format((bint+aint)*(bint+aint)))