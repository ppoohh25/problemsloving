"""
* * * * *
 * * * *
  * * *
   * *
    *
   * *
  * * *
 * * * *
* * * * *
"""
n = int(input())
a = []
for i in range(n):
    a.append('{}{}*'.format(' '*i,'* '*(n-1-i)))
for i in a:
    print(i)
for i in a[::-1]:
    if i == a[len(a)-1]:
        pass
    else:
        print(i)