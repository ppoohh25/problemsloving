a = list(input())
count = 0
for i in a:
  if i.isupper() == True:
    count+=1
  if i == '2':
    count+=1
  if i == '3':
    count+=2
  if i == '4':
    count+=3
print(count)