
x = int(input())
for i in range(x):
    word = input()
    if word[0:2] == '%%':
        print(word[2:])
    elif word[0:4] == '####':
        i += 1
    else:
        print(word)
