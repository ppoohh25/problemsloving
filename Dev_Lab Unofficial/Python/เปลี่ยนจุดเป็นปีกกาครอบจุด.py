a = list(input())
new_as = []
for a in a:
    new_a = a.replace(".", "[.]")
    new_as.append(new_a)
join = ''.join(new_as)
print(join)