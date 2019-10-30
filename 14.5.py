s = input()
key = input()
i = s.find(key) + len(key) + 1
while s[i] != '&' and s[i] != '=' and s[i] != '?' and s[i] != '#':
    print(s[i], end='')
    i += 1
