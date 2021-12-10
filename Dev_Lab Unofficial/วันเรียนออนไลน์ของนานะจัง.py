must = [1,2,3,4,5,6,7,8]
do = list(map(str,input().split(',')))

for i in range(len(do)):
  if do[i] == 'study math online':
    do[i] = 1
  elif do[i] == 'learn English online':
    do[i] = 2
  elif do[i] == 'learn Thai online':
    do[i] = 3
  elif do[i] == 'study science online':
    do[i] = 4
  elif do[i] == 'read test preparation o-net':
    do[i] = 5
  elif do[i] == 'do housework':
    do[i] = 6
  elif do[i] == 'learn to draw':
    do[i] = 7
  elif do[i] == 'learn to sing':
    do[i] = 8

still = len(must)-len(do)
undo = list(set(must)-set(do))
undo.sort()
print('There is still {} things to do.'.format(still))
for i in range(len(undo)):
  if undo[i] == 1:
    undo[i] = 'study math online'
  if undo[i] == 2:
    undo[i] = 'learn English online'
  if undo[i] == 3:
    undo[i] = 'learn Thai online'
  if undo[i] == 4:
    undo[i] = 'study science online'
  if undo[i] == 5:
    undo[i] = 'read test preparation o-net'
  if undo[i] == 6:
    undo[i] = 'do housework'
  if undo[i] == 7:
    undo[i] = 'learn to draw'
  if undo[i] == 8:
    undo[i] = 'learn to sing'

for i in undo:  
  print('- {}'.format(i))