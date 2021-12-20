a = []
while True:
  i = int(input())
  if i <= 0:
    break
  else:
    a.append(i)
print(sum(a)/len(a))