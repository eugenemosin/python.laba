m = int(input())
eda = set()
eda2 = set()
for i in range(m):
    eda.add(input())
n = int(input())
for i in range(n):
    kolvo_blud = int(input())
    for y in range(kolvo_blud):
        eda2.add(input())
for elem in (eda - eda2):
    print(elem)

