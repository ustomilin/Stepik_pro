from collections import Counter

def scrabble(symbols, word):
    for i, j in Counter(word.lower()).items():
        if Counter(symbols.lower())[i] < j:
            return False
    return True


print(scrabble('gEEkBEE', 'beegeek'))