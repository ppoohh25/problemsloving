n = int(input())
a = []
b = 0
for i in range(1,n+1):
  if i%2 == 0:
    b += i**2
    
print(b)