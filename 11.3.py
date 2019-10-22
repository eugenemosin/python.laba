word = input()
x = int(input())
bukva = input()
if x < 1 or x > len(word) + 1 or  len(bukva) > 1:
    print('ОШИБКА')
elif word[x-1] == bukva:
    print('ДА')
else:
    print('НЕТ')
