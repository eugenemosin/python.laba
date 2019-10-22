n = int(input())
cat = False
for i in range(n):
    x = input()
    if 'кот' in x or 'Кот' in x:
        cat = True
if cat:
    print('МЯУ')
else:
    print('Нет кота :с')

