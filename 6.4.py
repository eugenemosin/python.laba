# Сравнение IQ n-ого человека со средним IQ предыдущих измерений
n = int(input())
siq = 0
sn = 0
for i in range(n):
    iq = int(input())
    siq += iq
    sn += 1
    if iq > (siq / sn):
        print('>')
    elif iq < (siq / sn):
        print('<')
    else:
        print(0)
