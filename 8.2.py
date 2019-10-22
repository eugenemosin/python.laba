columns = int(input())
strings = int(input())
sym = input()

for j in range(1, strings + 1):
    for i in range(1, columns + 1):
        if (j == 1) or (j == strings):
            print(sym, end='\t')
        elif (i == 1) or (i == columns):
            print(sym, end='\t')
        else:
             print(' ', end='\t')
    print()
