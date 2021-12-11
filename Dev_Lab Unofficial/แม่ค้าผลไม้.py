x = str(x).split()
for i in range(x.index('A:'),x.index('B:')):
  A.append(x[i])
for i in range(x.index('B:'),x.index('C:')):
  B.append(x[i])
for i in range(x.index('C:'),len(x)):
  C.append(x[i])
A.pop(0)
B.pop(0)
C.pop(0)
for i in range(len(A)):
  for j in range(i+1,len(A)):
    if A[i] == A[j]:
      sA += 1
for i in range(len(B)):
  for j in range(i+1,len(B)):
    if B[i] == B[j]:
      sB += 1
sB1 = len(B)-sB



if len(A)> sB1 and len(A) > len(C):
  print('A')
if sB1 > len(A) and sB1 > len(C):
  print('B')
if len(C) > len(A) and len(C) > sB1:
  print('C')