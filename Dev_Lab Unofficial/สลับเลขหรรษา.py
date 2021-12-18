a = list(input())
b = input()
c = list(input())

a = int(''.join(a[::-1]))
c = int(''.join(c[::-1]))

print('{} {} {} = {}'.format(a,b,c,a+c))