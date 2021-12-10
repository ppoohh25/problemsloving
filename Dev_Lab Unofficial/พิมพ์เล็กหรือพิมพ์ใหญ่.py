word = list(input())
up = 0
low = 0
for i in range(len(word)):
  if word[i].isupper() == True:
    up += 1
  else:
    low += 1
print('UPPER:{}'.format(up))
print('LOWER:{}'.format(low))