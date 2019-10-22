# Вывод кол-ва камней в каждой куче после операции
kucha1 = int(input())
kucha2 = int(input())
while kucha1 != 0 or kucha2 != 0:
    numofkucha = int(input())  # Номер кучи из которой берем камни
    numofstones = int(input())  # Кол-во камней взятых из кучи
    if numofkucha == 1:
        kucha1 -= numofstones
    elif numofkucha == 2:
        kucha2 -= numofstones
    print(kucha1, kucha2)
