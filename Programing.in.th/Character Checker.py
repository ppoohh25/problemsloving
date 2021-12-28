word = list(input())
C = 0
S = 0
for i in range(len(word)):
    if word[i].isupper() == True:
        C += 1
    if word[i].islower() == True:
        S +=1
if C > 0 and S == 0:
    print('All Capital Letter')
if S > 0 and C == 0:
    print('All Small Letter')
if S != 0 and C != 0:
    print('Mix')