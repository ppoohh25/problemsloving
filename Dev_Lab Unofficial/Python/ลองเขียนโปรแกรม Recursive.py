n = int(input())
def f(n):
  if n < 0:
    return -1
  if n == 0 :
    return 1
  else :
    return f(n-1)+100
print(f(n))