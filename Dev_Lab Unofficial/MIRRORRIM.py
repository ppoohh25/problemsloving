w = list(input())
a = []
for i in range(0,len(w)-1):
  a.append(w[i])

print(''.join(w)+''.join(a[::-1]))