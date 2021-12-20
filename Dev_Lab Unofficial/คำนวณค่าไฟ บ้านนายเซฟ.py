a = input().split(':')
b = input().split(':')
c = input().split(':')

a = int(a[1])
b = int(b[1])
c = int(c[1])

costa = 0.12*a*3
costb = 0.5*b*3
costc = 0.06*c*3

print("{:.2f}".format(costa+costb+costc))