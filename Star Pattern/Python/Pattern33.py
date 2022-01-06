"""
* * *
*   *
*   *
*   *
 ***
*   *
*   *
*   *
* * *
"""
n = int(input())
a = []
for i in range(n):
    if i == 0:
        a.append('* * *')
    elif i == n-1:
        a.append(' ***')
    else:
        a.append('*   *')
for i in a:
    print(i)
for i in a[::-1]:
    if i == a[len(a)-1]:
        pass
    else:
        print(i)