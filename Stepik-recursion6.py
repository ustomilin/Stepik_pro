def get_pow(a, n):
    if n == 0:
        return 1
    else:
        print(a, n)
        return a * get_pow(a, n - 1)


print(get_pow(2, 21))
