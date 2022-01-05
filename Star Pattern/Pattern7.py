"""
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
"""
n = int(input())
a = []
for i in range(n):
    a.append('{}{}*{}'.format(' '*int(n-1-i),'*'*i,'*'*i))
for i in a:
    print(i)
for i in a[::-1]:
    if i == a[len(a)-1]:
        pass
    else:
        print(i)