import math
a = list(map(int,input().split()))
price = list(map(int,input().split()))

b = 0

for i in range(a[0]):
  b += price[i]+int(math.ceil(price[i]*a[1]/100))
print(b)