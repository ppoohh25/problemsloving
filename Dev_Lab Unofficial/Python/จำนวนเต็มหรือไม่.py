a = float(input())

root = a**0.5
inroot = int(root)
if root - inroot == 0 :
  print('Integer')
else:
  print('Float')