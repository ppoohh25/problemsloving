a = input()
b = input()
li = list(map(str,a.split(b)))

li[0] = li[0]+b
for i in range(1,len(li)-1):
  li[i] = b+li[i]+b
li[len(li)-1] = b+li[len(li)-1]
for i in range(len(li)):
  print(li[i])
