a = list(map(int,input().split()))
b = []
#ace
A = a[0]*a[2]*a[4]
b.append(str(A))
#acf + ade + bce
B = (a[0]*a[2]*a[5])+(a[0]*a[3]*a[4])+(a[1]*a[2]*a[4])
b.append(str(B))
#adf + bcf + bde
C = (a[0]*a[3]*a[5])+(a[1]*a[2]*a[5])+(a[1]*a[3]*a[4])
b.append(str(C))
#bdf
D = a[1]*a[3]*a[5]
b.append(str(D))
print(' '.join(b))