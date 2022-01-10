w = int(input())
h2 = (int(input())/100)**2
bmi = w/h2
print('{:.2f}'.format(bmi))
if bmi < 18:
  print('Thin')
elif 18 <= bmi <= 22:
  print('Good Health')
elif 23 <= bmi <= 24:
  print('Fat Level 1')
elif 25 <= bmi <= 29:
  print('Fat Level 2')
elif bmi > 30:
  print('Fat Level 3')