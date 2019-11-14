def prime(number):
    if (number % 2 == 0) or (number % 3 == 0) or (number % 5 == 0) or (number % 7 == 0) or (number % 11 == 0):
        if number == 2 or number == 3 or number == 5 or number == 7:
            return "простое"
        return "составное"
    else:
        return "простое"
print(prime(169))
