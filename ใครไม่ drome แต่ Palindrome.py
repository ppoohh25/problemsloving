a= list(input())
b="".join(map(str,a))
if a == a[::-1]:
  print('{} is a palindrome.'.format(b))
else:
  print('{} is not a palindrome.'.format(b))
