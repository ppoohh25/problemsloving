price = int(input())
pay = int(input())
a = []
for i in range(6):
  a.append(input().split())
thousand = int(a[0][1])
fivehundred = int(a[1][1])
hundred = int(a[2][1])
fifty = int(a[3][1])
twenty = int(a[4][1])
ten = int(a[5][1])
change = pay - price
print('change: {}'.format(change))

if change > 1000 and thousand > 0:
    b = change//1000
    if b > thousand:
      b = thousand
      change -= 1000*b
      print('cash: 1000 amount: {}'.format(b))
    else:
      change -= 1000*b
      print('cash: 1000 amount: {}'.format(b))
      
if change > 500 and fivehundred > 0:
    b = change//500
    if b > fivehundred:
      b = fivehundred
      change -= 500*b
      print('cash: 500 amount: {}'.format(b))
    else:
      change -= 500*b
      print('cash: 500 amount: {}'.format(b))

if change > 100 and hundred > 0:
    b = change//100
    if b > hundred:
      b = hundred
      change -= 100*b
      print('cash: 100 amount: {}'.format(b))
    else:
      change -= 100*b
      print('cash: 100 amount: {}'.format(b))

if change > 50 and fifty > 0:
    b = change//50
    if b > fifty:
      b = fifty
      change -= 50*b
      print('cash: 50 amount: {}'.format(b))
    else:
      change -= 50*b 
      print('cash: 50 amount: {}'.format(b))
      
if change > 20 and twenty > 0:
    b = change//20
    if b > twenty:
      b = twenty
      change -= 20*b
      print('cash: 20 amount: {}'.format(b))
    else:
      change -= 20*b
      print('cash: 20 amount: {}'.format(b))
      
if change >= 10 and ten > 0:
    b = change//10
    if b > ten:
      b = ten
      change -= 10*b
      print('cash: 10 amount: {}'.format(b))
    else:
      change -= 10*b
      print('cash: 10 amount: {}'.format(b))