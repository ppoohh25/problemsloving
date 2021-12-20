a = []
b = 0
for i in range(3):
  a.append(input().split())
for i in range(3):
  if a[i][0] == 'Dog':
    b += int(a[i][1])*4
  if a[i][0] == 'Cat':
    b += int(a[i][1])*4
  if a[i][0] == 'Chicken':
    b += int(a[i][1])*2
  if a[i][0] == 'Duck':
    b += int(a[i][1])*2
  if a[i][0] == 'Cow':
    b += int(a[i][1])*4
  if a[i][0] == 'Snake':
    b += int(a[i][1])*0
  if a[i][0] == 'Bird':
    b += int(a[i][1])*2
print(b)