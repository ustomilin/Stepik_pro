def move_zeros(lst: list):
    x = lst.count(0)
    lst = list(filter(lambda x: x != 0, lst))
    lst.extend([0]*x)
    return lst

print(move_zeros([1, 0, 1, 2, 0, 1, 3]))