n = int(input())
income = []
tax = 0
for i in range(n):
  income.append(int(input()))
for i in income:
  if i >= 0 and i <=100000:
    tax += 0
  if i >= 100001 and i <= 300000:
    tax += (i*0.1)
  if i >= 300001 and i <= 500000:
    tax += (i*0.15)
  if i >= 500001 and i <= 1000000:
    tax += (i*0.2)
  if i > 1000000 :
    tax += (i*0.25)
if tax == 0:
  print('ไม่ต้องเสียภาษี')
else:
  print('เสียภาษีทั้งหมด {} กะลา'.format(int(tax)))