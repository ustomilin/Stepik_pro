def vnut(n, x=16):
    print(' ' * ((n - 1) * 2), str(n) * x, sep='')
    if n < 4:
        vnut(n + 1, x - 4)
        print(' ' * ((n - 1) * 2), str(n) * x, sep='')


vnut(1)
