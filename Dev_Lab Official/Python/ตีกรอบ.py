a = int(input())
if a >= 2:
  print('{}'.format('#'*a))
  for i in range(a-2):
    print('#{}#'.format(' '*int(a-2)))
  print('{}'.format('#'*a))
if a ==1 :
  print('#')