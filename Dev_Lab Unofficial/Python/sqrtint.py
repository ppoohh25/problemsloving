n = int(input())
if n == -1:
  print('i')
elif n < 0:
  print('false')
elif int(n**0.5)**2 == n:
  print(int(n**0.5))
else:
  print('false')