typ = input()
size = input()
color = input()
clo = input()
n = int(input())
typname = ''
sizename = ''
colorname = ''
cloname = ''
price1 = 0
price2 = 0
price3 = 0
price4 = 0
#ประเภท
if typ == '1':
  price1 += 20
elif typ == '2':
  price1 += 30
elif typ == '3':
  price1 += 30
elif typ == '4':
  price1 += 40
elif typ == '5':
  price1 += 40
#ชื่อประเภท
if typ == '1':
  typename = 'underwear'
elif typ == '2':
  typename = 'pants'
elif typ == '3':
  typename = 'skirt'
elif typ == '4':
  typename = 'shirt'
elif typ == '5':
  typename = 'blouse'
print('{} - {}'.format(typename,price1))
#size
if size == '1':
  price2 += 5
elif size == '2':
  price2 += 10
elif size == '3':
  price2 += 15
elif size == '4':
  price2 += 20
elif size == '5':
  price2 += 25
#sizename
if size == '1':
  sizename = 'S'
elif size == '2':
  sizename = 'M'
elif size == '3':
  sizename = 'L'
elif size == '4':
  sizename = 'XL'
elif size == '5':
  sizename = 'XXL'
print('size {} - {}'.format(sizename,price2))
#color
if color == 'R':
  price3 += 15
elif color == 'B':
  price3 += 15
elif color == 'W':
  price3 += 10
elif color == 'G':
  price3 += 15
elif color == 'BK':
  price3 += 15
#name color
if color == 'R':
  colorname = 'red'
elif color == 'B':
  colorname = 'blue'
elif color == 'W':
  colorname = 'white'
elif color == 'G':
  colorname = 'green'
elif color == 'BK':
  colorname = 'black'
print('color {} - {}'.format(colorname,price3))
#เนื้อผ้า
if clo == '1':
  price4 += 20
elif clo == '2':
  price4 += 15
elif clo == '3':
  price4 += 25
elif clo == '4':
  price4 += 30
elif clo == '5':
  price4 += 25

if clo == '1':
  cloname = 'cotton'
elif clo == '2':
  cloname = 'nylon'
elif clo == '3':
  cloname = 'spandex'
elif clo == '4':
  cloname = 'wool'
elif clo == '5':
  cloname = 'linen'
print('{} - {}'.format(cloname,price4))
print('amount - {}'.format(n))
allprice =price1+price2+price3+price4
print('cost - {}*{} = {}'.format(allprice,n,allprice*n))

