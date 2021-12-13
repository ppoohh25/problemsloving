a = int(input())
if a > 2:
  print('{}'.format('#'*a))
  for i in range(a-2):
    print('#{}#'.format(' '*int(a-2)))
  print('{}'.format('#'*a))
else:
  print("Box's height must be more than 2")