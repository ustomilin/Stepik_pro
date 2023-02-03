def recursive_sum(a, b):
    if a >= 1:
        return 1 + recursive_sum(a - 1, b)
    if b >= 1:
        return 1 + recursive_sum(a, b - 1)
    return 0


print(recursive_sum(99, 0))
