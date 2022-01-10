a = list(map(float,input().split()))
f = (a[0]*a[1])/(a[0]+a[1])
print('{:.2f} cm'.format(f))
if f > 0:
  print('เลนส์นูน')
else:
  print('เลนส์เว้า')