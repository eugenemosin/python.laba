columns = int(input())
strings = int(input())

for j in range(1, strings+1):
    for i in range(1, columns+1):
        print(i / j, end='\t')
    print()
