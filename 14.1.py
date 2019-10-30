n = int(input())
vivod = []
for i in range(n):
    x = input()
    if 'лук' not in x:
        vivod.append(x)
print(', '.join(vivod))
