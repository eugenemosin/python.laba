n = int(input())
list = []
for i in range(n):
    list.append(input())
print(sorted(list, key=int, reverse=True))

