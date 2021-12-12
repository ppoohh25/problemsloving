code = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
word = list(input())
a = []
for i in range(len(word)):
  for j in range(len(code)):
    if word[i] == code[j]:
      a.append(j+1)
for i in range(len(a)):
  a[i] = str(a[i])
print(''.join(a))
