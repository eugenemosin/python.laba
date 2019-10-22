x = int(input())
str = input()
for i in range(len(str)):
     print(chr((ord(str[i]))+x))
