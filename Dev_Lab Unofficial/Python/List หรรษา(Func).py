a = list(input())
b=[]
int1 = int(a[1])
int2 = int(a[3])
int3 = int(a[5])
b.append(int1)
b.append(int2+int1)
b.append(int1+int2+int3)
print(b)