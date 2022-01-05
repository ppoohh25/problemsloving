from itertools import permutations

a = input().split()
b = int(a[1])

c = list(permutations(a[0],b))
c.sort()
for i in c:
    print(''.join(i))