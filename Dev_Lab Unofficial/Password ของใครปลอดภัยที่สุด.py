a = list(map(str,input().split(',')))
num = ['1','2','3','4','5','6','7','8','9','0']
s = ['$','#','@']
Man = list(a[0])
Non = list(a[1])
Miv = list(a[2])
Manu = 0
Manl = 0
Mann = 0
Mans = 0
Nonu = 0
Nonl = 0
Nonn = 0
Nons = 0
Mivu = 0
Mivl = 0
Mivn = 0
Mivs = 0
Manscore = 0
Nonscore = 0
Mivscore = 0
x = []
for i in range(len(Man)):
  if Man[i].islower() == True:
    Manscore += 1
    Manl +=1
  if Man[i].isupper() == True:
    Manscore += 1
    Manu +=1
  if Man[i] in num:
    Manscore += 1
    Mann +=1
  if Man[i] in s:
    Manscore += 1
    Mans +=1
for i in range(len(Non)):
  if Non[i].islower() == True:
    Nonscore += 1
    Nonl += 1
  if Non[i].isupper() == True:
    Nonscore += 1
    Nonu += 1
  if Non[i] in num:
    Nonn +=1
    Nonscore += 1
  if Non[i] in s:
    Nons += 1
    Nonscore += 1
for i in range(len(Miv)):
  if Miv[i].islower() == True:
    Mivl +=1
    Mivscore += 1
  if Miv[i].isupper() == True:
    Mivu += 1
    Mivscore += 1
  if Miv[i] in num:
    Mivn += 1
    Mivscore += 1
  if Miv[i] in s:
    Mivs += 1
    Mivscore += 1
if (len(Man) <6 and len(Man) >12) or Manu == 0 or Manl == 0 or Mann == 0 or Mans == 0: 
  Manscore = 0
if (len(Non) <6 and len(Non) >12) or Nonu == 0 or Nonl == 0 or Nonn == 0 or Nons == 0:
  Nonscore = 0
if (len(Miv) <6 and len(Miv) >12) or Mivu == 0 or Mivl == 0 or Mivn == 0 or Mivs == 0:
  Mivscore = 0

x.append(Manscore)
x.append(Nonscore)
x.append(Mivscore)

for i in range(1):
  if x[i] == max(x):
    print('{} (Man)'.format(''.join(Man)))
  if x[i+1]  == max(x):
    print('{} (Non)'.format(''.join(Non)))
  if x[i+2] == max(x):
    print('{} (Miv)'.format(''.join(Miv)))
