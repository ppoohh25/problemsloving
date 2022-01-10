money = int(input())
mon = money
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
if money > 1000:
  a = money//1000
  money -= a*1000
  print('ธนบัตร 1,000฿ : {} ฉบับ'.format(a))
if money > 500:
  b = money//500
  money -= b*500
  print('ธนบัตร 500฿ : {} ฉบับ'.format(b))
if money > 100:
  c = money//100
  money -= c*100
  print('ธนบัตร 100฿ : {} ฉบับ'.format(c))
if money > 50:
  d = money//50
  money -= d*50
  print('ธนบัตร 50฿ : {} ฉบับ'.format(d))
if money > 20:
  e = money//20
  money -= e*20
  print('ธนบัตร 20฿ : {} ฉบับ'.format(e))
if money > 10:
  f = money//10
  money -= f*10
  print('เหรียญ 10฿ : {} เหรียญ'.format(f))
if money > 5:
  g = money//5
  money -= g*5
  print('เหรียญ 5฿ : {} เหรียญ'.format(g))
if money > 0:
  h = money//1
  money -= h*1
  print('เหรียญ 1฿ : {} เหรียญ'.format(h))
print('จำนวนเงินที่แลกทั้งหมด {:,} บาท'.format(mon))