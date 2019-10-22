n = int(input())
buylist = []
for i in range(n):
    buylist.append(input())
    buylist[i] += ' ' + input()
# print(buylist[::-1])
for i in buylist[::-1]:
    print(i)
