n = int(input())
names = []
numbers = []
final = []
notfinal = []
x = 0
for i in range(n):
    names.append(input())
    k = int(input())
    x += k
    numbers.append(k)
x /= n
for i in range(n):
    if numbers[i] > x:
        final.append(names[i])
    else:
        notfinal.append(names[i])
final.sort()
notfinal.sort()
for i in range(len(final)):
    print(final[i])
for i in range(len(notfinal)):
    print(notfinal[i])
