f = list(map(int,input().split()))
s = list(map(int,input().split()))
o = []

if len(f) != len(s) or sum(f) > 32548 or sum(s) > 32548:
  print('Invalid')
else:
  for i in range(len(f)):
    o.append(f[i]+s[i])
  for i in range(len(o)):
    print(o[i], end = ' ')