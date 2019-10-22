whitelistnum = int(input())
whitelist = []
for i in range(whitelistnum):
    whitelist.append(input())
x = int(input())
for i in range(x):
    a = input()
    if a in whitelist:
        print(a)
