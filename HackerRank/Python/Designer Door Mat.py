N,M = map(int,input().split())
a = [('.|.'*(2*i+1)).center(M,'-') for i in range(N//2)]
print('\n'.join(a + ['WELCOME'.center(M, '-')] + a[::-1]))