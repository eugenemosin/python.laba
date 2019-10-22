summa = int(input())
kolvo = int(input())
y = 1
x1 = 0
y1 = 0
z1 = 0

for j in range(1, 4):
    x = j
    for y in (1, kolvo-x):
        z = kolvo - x - y
        if (x + y + z == kolvo) and ((x * 20) + (y * 10) + (z * 5) == summa):
            x1 = x
            y1 = y
            z1 = z
    print(x1, y1, z1)
