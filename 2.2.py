print('Введите логин')
log = input()
print('Введите адрес')
pas = input()
if '@' in log:
    print('Некорректный логин')
elif '@' not in pas:
    print('Некорректный адрес')
else:
    print('OK')
