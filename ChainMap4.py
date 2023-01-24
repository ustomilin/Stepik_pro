from collections import ChainMap


def get_value(chainmap: ChainMap, key, from_left = True):
    if from_left:
        try:
            return chainmap[key]
        except KeyError:
            return None
    else:
        chainmap.maps.reverse()
        try:
            return chainmap[key]
        except KeyError:
            return None

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'age'))