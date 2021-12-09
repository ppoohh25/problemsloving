a = int(input())
b = int(input())
c = int(input())

if a> b and a>c:
  print('MAX :',a)
elif b>a and b>c:
  print('MAX :',b)
elif c>a and c>b:
  print('MAX :',c)
elif c==a and c==b:
  print('MAX :',c)
elif a==b and a==c:
  print('MAX :',a)
elif b==a or b==c:
  print('MAX :',b)