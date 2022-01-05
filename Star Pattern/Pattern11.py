"""
*****
 *****
  *****
   *****
    *****
"""
n = int(input())
a = []
for i in range(n):
    a.append('{}*****'.format(' '*int(n-1-i)))
for i in a[::-1]:
    print(i)