# Обратный отсчет
n = int(input())
if n < 0:
    print('Пуск!')
else:
    for i in range(n):
        print('Осталось секунд:', n-i)
    print('Осталось секунд: 0')
    print('Пуск!')
