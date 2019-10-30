s = input()
x = 1
result = 0
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        x += 1
    else:
        if result < x:
            result = x
            x = 0
print(result)
