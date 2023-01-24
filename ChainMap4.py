from collections import ChainMap


def deep_update(chainmap: ChainMap, key, value):
    x = chainmap.maps
    count = 0
    for i in range(len(x)):
        if key in x[i]:
            x[i][key] = value
            count += 1
    if count == 0:
        chainmap[key] = value


chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
deep_update(chainmap, 'age', 20)

print(chainmap)