a = list(input())
I = 0
V = 0
X = 0
for i in range(len(a)):
  if 'I' == a[i]:
    I+=1
  if 'V' == a[i]:
    V+=1
  if 'X' == a[i]:
    X+=1
if X > 3 or V > 3 or I > 3:
  print('Not Correct')
else:
  print('Correct')