"""
    *
   * *
  *   *
 *     *
*********
"""
n = int(input())
print('{}*'.format(' '*int(n-1)))
for i in range(n-1):
    if i == 0:
        pass
    else:
        print('{}*{}*'.format(' '*int(n-i-1),' '*int(2*i-1)))
print('*'*int(2*n-1))