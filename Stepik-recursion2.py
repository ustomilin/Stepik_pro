def kol_cifr(n):
    if n // 10 == 0:
        return 1
    else:
        return kol_cifr(n//10) + 1


print(kol_cifr(int(input())))
