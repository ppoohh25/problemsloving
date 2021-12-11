rule = input().split()
score = 0
for i in range(len(rule)):
  rule[i] = int(rule[i])
  
fi = list(input())
se = list(input())

for i in range(rule[0]):
  if fi[i] == se[i]:
    score += rule[1]
  if fi[i] != se[i] and se[i] != 'X':
    score = score - rule[2]
  if se[i] == 'X':
    score += rule[3]
print('Your score:{}'.format(score))