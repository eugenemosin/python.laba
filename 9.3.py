org = []
n = int(input())
res = 0
for i in range(n):
    org.append(input())
for x in set(org):
    k = 0
    for y in org:
        if x == y:
            k += 1
    if k > 1:
        res += k
print(res)

