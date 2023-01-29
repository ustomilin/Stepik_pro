def get_fast_pow(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return get_fast_pow(a * a, n // 2)
    else:
        return a * get_fast_pow(a, n - 1)

print(get_fast_pow(10, 20))
