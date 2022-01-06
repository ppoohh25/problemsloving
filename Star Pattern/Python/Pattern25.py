"""
*****
 *   *
  *   *
   *   *
    *****
"""
n = int(input())
print('*****')
for i in range(1,n-1):
    print('{}*   *'.format(' '*int(i)))
print('{}*****'.format(' '*int(n-1)))