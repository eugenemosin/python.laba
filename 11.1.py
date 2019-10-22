word = input()
k = 1
res = 0
for i in range(len(word)-1):
    if word[i] == 'о' and word[i+1] == 'о':
        k += 1
        res = k
    else:
        k = 1
print(res)
