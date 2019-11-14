def ask_password():
    passsword = "password"
    for i in range(3):
        stroka = input("Введите пароль: ")
        if stroka == passsword:
            return ("Пароль принят")
        if i == 2 and stroka != passsword:
            return ("В доступе отказано")
print(ask_password())

