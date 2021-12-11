name = input()
pas = input()
lname = input()
lpas = input()

rn = name.replace(' ','')
rp = pas.replace(' ','')
rln = lname.replace(' ','')
rlp = lpas.replace(' ','')

sn = rn.split(':')
sp = rp.split(':')
sln = rln.split(':')
slp = rlp.split(':')

if sn[1] == sln[1] and sp[1] == slp[1]:
  print('Success')
else:
  print('Error')