a = int(input())
if a%3 == 0 and a%2 == 0:
  print('FizzBuzz')
elif a%3 == 0 and a%2 != 0:
  print('Fizz')
elif a%3 != 0 and a%2 == 0:
  print('Buzz')