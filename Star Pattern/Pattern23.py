"""
     *
   * *
  *  *
 *   *
*    *
 *   *
  *  *
   * *
     *
"""
n = int(input())
a = []
for i in range(n):
    if i == 0:
        a.append('{}*'.format(' '*int(n+1)))
    elif i == 1:
        a.append('{}{}{}*'.format(' '*int(n-1),'*'*int(i-(i-1)),' '*int(i)))
    else:
        a.append('{}{}{}*'.format(' '*int(n-(i)),'*'*int(i-(i-1)),' '*int(i)))
for i in a:
    print(i)
for i in a[::-1]:
    if i == a[len(a)-1]:
        pass
    else:
        print(i)