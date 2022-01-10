a = list(input())
upper = 0
lower = 0
num = 0
sign = 0
for i in range(len(a)):
  if len(a) < 3 or len(a) > 20 :
    break
  if a[i].isupper() == True:
    upper+=1
  if a[i].islower() == True:
    lower+=1
  if a[i] == '0' or a[i] == '1' or a[i] == '2' or a[i] == '3' or a[i] == '4' or a[i] == '5' or a[i] == '6' or a[i] == '7' or a[i] == '8' or a[i] == '9':
    num+=1
  if a[i] == '@' or a[i] == '!' or a[i] == '/' or a[i] == '[' or a[i] == ']' or a[i] == ';' or a[i] == '-' or a[i] == '|' or a[i] == '*' or a[i] == '^' or a[i] == "'" or a[i] == '"':
    sign+=1
if upper !=0 and lower != 0 and num != 0 and sign !=0:
  print('Valid')
else:
  print('Invalid')