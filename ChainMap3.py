from collections import ChainMap


def get_all_values(chainmap: ChainMap, key):
    mn = []
    for i in chainmap.maps:
        if key in i:
            mn.append(i[key])
    return set(mn)


chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
result = get_all_values(chainmap, 'name')

print(*sorted(result))
