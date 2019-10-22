pas = input()
if len(pas) < 8:
    print('Короткий!')
else:
    pas2 = input()
    if '123' in pas:
        print('Простой!')
    elif pas != pas2:
        print('Различаются.')
    else:
        print('OK')
