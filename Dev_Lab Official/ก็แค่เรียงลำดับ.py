a = []
for i in range(5):
  a.append(int(input()))
#join = ''.join(a)
a.sort()
b = a[::-1]
for i in range(len(a)):
  
  print(b[i])