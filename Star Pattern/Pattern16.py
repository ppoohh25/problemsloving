"""
     *
   * *
  *  *
 *   *
******
"""
n = int(input())
for i in range(n):
    if i == 0:
        print('{}*'.format(' '*int(n+1)))
    elif i == 1:
        print('{}{}{}*'.format(' '*int(n-1),'*'*int(i-(i-1)),' '*int(i)))
    else:
        print('{}{}{}*'.format(' '*int(n-(i)),'*'*int(i-(i-1)),' '*int(i)))
print('*'*int(n+2))