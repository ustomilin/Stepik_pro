from collections import Counter
from sys import stdin

def count_items(list_of_items):
    count_all = Counter(list_of_items)
    for item, count in sorted(count_all.items()):
        print(f'{item}: {count}')



count_items(input().split(','))