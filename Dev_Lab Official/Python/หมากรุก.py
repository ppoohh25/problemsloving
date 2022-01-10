a = []
b = []
score = 0
for i in range(8):
  a.append(list(input()))
for i in range(8):
  for j in range(8):
    if a[i][j] == '.':
      pass
    else:
      b.append(a[i][j])
for i in range(len(b)):
  if b[i] == 'P':
    score += 1
  elif b[i] == 'N':
    score += 3
  elif b[i] == 'B':
    score += 3
  elif b[i] == 'R':
    score += 5
  elif b[i] == 'Q':
    score += 9
  elif b[i] == 'K':
    score += 0
  elif b[i] == 'p':
    score -= 1
  elif b[i] == 'n':
    score -= 3
  elif b[i] == 'b':
    score -= 3
  elif b[i] == 'r':
    score -= 5
  elif b[i] == 'q':
    score -= 9
  elif b[i] == 'k':
    score -= 0

if score == 0:
  print('equal')
else:
  print(score)