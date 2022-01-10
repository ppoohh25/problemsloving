magic = input()

a = ['Fire','Water','Wind','Ground','Light','Dark']

if magic not in a:
  print('No have this mahou in your library.')
else:
  b = a.index(magic)
  print('{0:020b}'.format(b))