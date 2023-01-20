from collections import Counter


def words_len(text):
    text = Counter(list(map(len, text.split())))
    for word_len, count in sorted(text.items(), key=lambda i: i[1]):
        print(f'Слов длины {word_len}: {count}')


words_len(input())
