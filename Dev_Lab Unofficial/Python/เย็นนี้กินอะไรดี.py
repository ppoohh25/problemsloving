fa = list(input())
ma = list(input())
bro = list(input())
sis = list(input())
n = 0
c = 0
for i in range(len(fa)):
  if fa[i].isupper() == True:
    fa[i] = fa[i].lower()
for i in range(len(ma)):
  if ma[i].isupper() == True:
    ma[i] = ma[i].lower()
for i in range(len(bro)):
  if bro[i].isupper() == True:
    bro[i] = bro[i].lower()
for i in range(len(sis)):
  if sis[i].isupper() == True:
    sis[i] = sis[i].lower()

jfa = ''.join(fa)
jma = ''.join(ma)
jbro = ''.join(bro)
jsis = ''.join(sis)
if jfa == 'chicken rice':
  c +=1
if jma == 'chicken rice':
  c += 1
if jbro == 'chicken rice':
  c += 1
if jsis == 'chicken rice':
  c += 1
if jfa == 'noodle':
  n +=1
if jma == 'noodle':
  n += 1
if jbro == 'noodle':
  n += 1
if jsis == 'noodle':
  n += 1

if n > c:
  print('Noodle')
if c > n:
  print('Chicken rice')
if n == c:
  print('Chicken rice')