n = int(input())
soldier = []
for i in range(n):
    soldier.append(input())
k = int(input())
d = []
while 1:
    if len(soldier) > 0:
        d.append(soldier[0])
        soldier.pop(0)
        n -= 1
    else:
        break
    t = 1
    for i in range(n // k):
        d.append(soldier[((i + 1) * k) - t])
        soldier.pop(((i + 1) * k) - t)
        n -= 1
        t += 1
for i in range(len(d)):
    print(d[i])
