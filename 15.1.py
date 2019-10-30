n = input()
s = input()
s = s.split()
for i in range(len(s)):
    if n.lower() in s[i].lower():
        print(s[i])
