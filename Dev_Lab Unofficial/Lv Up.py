a = list(map(str,input().split()))
exp = int(a[1])
maxexp = 100
lv = 1
hp = 100
atk = 10

while exp >= maxexp:
  a = exp//maxexp
  exp -= maxexp
  maxexp = 100+100*lv
  lv +=1
hp = hp*lv
atk = atk*lv
print('Lv : {}'.format(lv))
print('Exp : {}/{}'.format(exp,maxexp))
print('ATK : {}'.format(atk))
print('HP : {}'.format(hp))