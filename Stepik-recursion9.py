def is_power(number):
    print(number)
    if number % 2 == 0 and is_power(number//2) == True:
        return True
    elif number == 1:
        return True
    else:
        return False

print(is_power(511))