num = list(map(int,input().split()))
word = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
a = []
for i in range(len(num)):
  a.append(word[num[i]-1])
print(''.join(a))