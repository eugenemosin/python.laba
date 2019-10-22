x = input()
n = 0
cat = -1
while x != 'СТОП':
    n += 1
    if ('кот' in x) and (cat == -1):
        cat = n
    x = input()
print(cat)
