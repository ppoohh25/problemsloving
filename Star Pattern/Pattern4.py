"""
*****
 ****
  ***
   **
    *
"""
n = int(input())
for i in range(n):
    print('{}{}'.format(' '*int(i),'*'*int(n-i)))