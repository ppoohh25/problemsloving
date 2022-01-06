"""
******
 *   *
  *  *
   * *
     *
"""
n = int(input())
print('*'*int(n+2))
for i in range(1,n):
    print('{}{}{}*'.format(' '*i,'*'*int(i-(i-1)),' '*int(n-i)))
print('{}*'.format(' '*int(n+1)))