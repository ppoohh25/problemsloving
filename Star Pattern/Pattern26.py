"""
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
"""
n = int(input())
a = []
for i in range(n):
    x = ' '*int(n*2-((i+1)*2))
    a.append(x.center(n*2,'*'))
for i in a:
    print(i)
for i in a[::-1]:
    if i == a[len(a)-1]:
        pass
    else:
        print(i)