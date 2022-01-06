"""
    *****
   *   *
  *   *
 *   *
*****
"""
n = int(input())
print('{}*****'.format(' '*int(n-1)))
for i in range(n-2):
    print('{}*   *'.format(' '*int(n-i-2)))
print('*****')