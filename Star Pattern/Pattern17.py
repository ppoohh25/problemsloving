"""
******
*   *
*  *
* *
*
"""
n = int(input())
print('*'*int(n+1))
for i in range(n-1):
    if i == n-2:
        print('*')
    else:
        print('*{}{}'.format(' '*int(n-2-i),'*'*int(i-(i-1)))) 