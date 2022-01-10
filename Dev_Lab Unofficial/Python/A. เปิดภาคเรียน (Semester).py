a = int(input())
minu = 60
b = minu-a
if b < 10:
  b = str(b)
  b = '0'+b
print('07:{}'.format(b))