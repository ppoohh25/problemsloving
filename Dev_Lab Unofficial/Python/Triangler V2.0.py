b = int(input())
h = int(input())

area = 0.5*b*h
if area == int(area):
  print('{} cm2'.format(int(area)))
else:
  print('{:.1f} cm2'.format(area))