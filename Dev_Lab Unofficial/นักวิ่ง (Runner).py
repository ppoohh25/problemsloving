a = list(map(int,input().split()))
b = list(map(int,input().split()))
n = 0
while a[0] < a[1]:
  a[0] += b[0]
  a[1] += b[1]
  n +=1
print(n)