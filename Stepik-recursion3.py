def sum_cifr(n):
    if n // 10 == 0:
        return n % 10
    else:
        return n % 10 + sum_cifr(n//10)


print(sum_cifr(int(input())))
