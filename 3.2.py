x = int(input())
y = int(input())
operation = input()
if operation == '+':
    print(x+y)
elif operation == '-':
    print(x-y)
elif operation == '*':
    print(x*y)
elif operation == '/' and y != 0:
    print(x/y)
else:
    print('888888')
