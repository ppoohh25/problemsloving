a = int(input())
b = []
for num in range(2,a+1):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
       b.append(num)
if len(b) != 0:
  print('จำนวนเฉพาะในช่วง 0 ถึง {}'.format(a))
  print('มีอยู่ {} จำนวน'.format(len(b)))
else:
  print('ไม่สามารถหาได้')
