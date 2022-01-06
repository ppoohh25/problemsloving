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
        a.append('*')
    else:
        a.append('*{}*'.format(' '*i))
for i in a:
    print(i)
for i in a[::-1]:
    if i == a[len(a)-1]:
        pass
    else:
        print(i)