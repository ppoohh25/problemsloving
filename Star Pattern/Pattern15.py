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
        print('*')
    else:
        print('*{}{}'.format(' '*i,'*'*int(i-(i-1))))
print('*'*int(n+2))