"""
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
"""
n = int(input())
a = []
for i in range(n):
    if i == 0:
        pass
    else:
        a.append('{}*{}*'.format(' '*int(n-i-1),' '*int(2*i-1)))
print('{}*'.format(' '*int(n-1)))
for i in a:
    print(i)
for i in a[::-1]:
    if i == a[len(a)-1]:
        pass
    else:
        print(i)
print('{}*'.format(' '*int(n-1)))