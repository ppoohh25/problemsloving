base = int(input())
high = int(input())
cal = 0.5*base*high
if cal%1 == 0:
  print('{} cm2'.format(int(cal)))
else :
  print('{:.1f} cm2'.format(cal))