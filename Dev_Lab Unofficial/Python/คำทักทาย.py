a = input().split(':')
a[0] = int(a[0])
name = input()
if 5 <= a[0] <= 11:
  print('Good morning, {}'.format(name))
elif 12 <= a[0] <= 17:
  print('Good afternoon, {}'.format(name))
elif 18 <= a[0]:
  print('Good evening, {}'.format(name))