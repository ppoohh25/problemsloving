a = int(input())
i = 0
name = []
age = []
gender = []
while i < a:
  name.append(input())
  age.append(2017-int(input()))
  gender.append(input())
  i+= 1
print('--Customers Information--')
for i in range(a):
  print('{} (age : {})'.format(name[i],age[i]))
