"""
*********
 *     *
  *   *
   * *
    *
"""
n = int(input())
print('*'*int(2*n-1))
a = []
for i in range(n-1):
    if i == 0:
        pass
    else:
        a.append('{}*{}*'.format(' '*int(n-i-1),' '*int(2*i-1)))
for i in a[::-1]:
    print(i)
print('{}*'.format(' '*int(n-1)))