a = int(input())
b = int(input())
c = int(input())
x = a + b + c
if 80 <= x <=100:
    print('A')
if 75 <= x <=79:
    print('B+')
if 70 <= x <= 74:
    print('B')
if 65 <= x <= 69:
    print('C+')
if 60 <= x <= 64:
    print('C')
if 55 <= x <= 59:
    print('D+')
if 50 <= x <= 54:
    print('D')
if 0 <= x <= 49:
    print('F')