from collections import Counter


def count_sym(file_name):
    with open(file_name, encoding='utf8') as f:
        f = f.read().lower()
        count = Counter(f)
        for sym, kol in sorted(count.items()):
            if sym.isalpha():
                print(f'{sym}: {kol}')


count_sym('pythonzen.txt')
