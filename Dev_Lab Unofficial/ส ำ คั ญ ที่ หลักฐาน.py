info = list(map(str,input().split(':')))
ask = list(map(str,input().split(':')))
if info[0] == ask[0]:
  if info[1] == ask[1]:
    print('T')
  else:
    print('F')
else:
  print('DS')
