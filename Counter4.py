from collections import Counter

def count_items(list_of_items):
    count_all = Counter(list_of_items)
    max_len_key= len(max(count_all.keys(), key = len))
    for item, count in sorted(count_all.items()):
        item_uc = sum(map(lambda i: ord(i) if i != ' ' else 0, list(item)))
        print(f'{item.ljust(max_len_key)}: {item_uc} UC x {count} = {item_uc*count} UC')



count_items(input().split(','))