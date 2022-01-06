"""
*   *
 * *
  *
 * *
*   *
"""
import math
n = int(input())
a = []
for i in range(math.ceil(n/2)):
    if i == math.ceil(n/2)-1:
        a.append('*'.center(n,' '))
    else:
        a.append('{}*{}*'.format(' '*i,' '*int(n-2-(i*2))))
for i in a:
    print(i)
for i in a[::-1]:
    if i == a[len(a)-1]:
        pass
    else:
        print(i)