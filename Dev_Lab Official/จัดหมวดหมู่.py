a = int(input())
b = int(input())
c = []
d = 0
for i in range(b):
  c.append(input().split())
for i in range(len(c)):
  c[i][0] = int(c[i][0])
  c[i][1] = int(c[i][1])
for i in range(len(c)):
    if c[i][d] <= a <= c[i][d+1]:
      print(c[i][2])