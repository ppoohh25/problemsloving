a = list(input())
for i in range(len(a)):
  if a[i].isupper() == True:
    a[i] = a[i].lower()
  else:
    a[i] = a[i].upper()
join = ''.join(a)
print(join)