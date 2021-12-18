word = list(input())
old = ''.join(word)
last = word[len(word)-1]
selast = word[len(word)-2]
rule = ['s', 'x', 'z']
vowel = ['a','e','i','o','u']
if last in rule:
  word.append('es')
elif (selast == 's' and last == 'h') or (selast == 'c' and last == 'h'):
  word.append('es')
elif last == 'y' and selast not in vowel:
  word[len(word)-1] = 'ies'
else:
  word.append('s')

print('{} -> {}'.format(old,''.join(word)))