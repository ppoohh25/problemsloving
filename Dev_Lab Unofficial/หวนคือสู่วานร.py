boxra = float(input())
handsize = float(input())
nut = float(input())
nutsize = float(input())
getnut = 0

while handsize < boxra and nut != 0:
  handsize += nutsize
  getnut += 1
  nut -= 1
if handsize > boxra:
  print(getnut -1)
else:
  print(getnut)