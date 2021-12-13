a = []
b = [8, 14, 112, 76, 2]
luck = 0
for i in range(5):
  a.append(int(input()))
for i in range(len(a)):
  for j in range(len(b)):
    if a[i] == b[j]:
      luck +=1
if luck >=3:
  print('You are lucky')
else:
  print('You are unlucky')