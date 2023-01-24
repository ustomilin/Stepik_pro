import json
from collections import ChainMap


with open('files/zoo.json', encoding='utf8') as zoo:
    zoo = ChainMap(*json.load(zoo))
    print(sum(zoo.values()))
