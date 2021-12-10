li = [1,2,3,5,7,9,11,13,15,17,19,21,23,25,27,29]
a = int(input())
for i in range(len(li)):
  index = 0
  if a == li[i]:
    index = li.index(a)
    print(index)
if a > 29:
  print('-1')