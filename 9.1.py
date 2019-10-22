home = set()
n1 = int(input())
n2 = int(input())
for i in range(n1):
    home.add(input())
for i in range(n2):
    if input() in home:
        print('YES')
    else:
        print('NO')
