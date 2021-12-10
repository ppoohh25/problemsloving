word = list(input())
asc = []
sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
for i in range(len(word)):
  asc.append(ord(word[i]))
for i in range(len(asc)):
  asc[i] = asc[i]**len(word)
for i in range(len(asc)):
  sum1 += asc[i]
x = [int(i) for i in str(sum1)]
for i in range(len(x)):
  sum2 += x[i]
y = [int(i) for i in str(sum2)]
for i in range(len(y)):
  sum3 += y[i]
z = [int(i) for i in str(sum3)]
for i in range(len(z)):
  sum4 += z[i]

print(sum4)