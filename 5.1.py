# Поиск дня недели по введенной дате
d = int(input())
m = int(input())
if m > 2:
    m -= 2
else:
    m += 10
cy = int(input())
c = cy // 100
y = cy % 100
x1 = (d + (13 * m - 1) // 5 + y + y // 4 + c // 4 - 2 * c + 777) % 7
print(x1)
