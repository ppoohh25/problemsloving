a = input()
b = [ord(c) for c in a]
for i in range(len(b)):
  b[i] = b[i]+4
res = ''.join(chr(i) for i in b)
print(res)