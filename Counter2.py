from collections import Counter

def count_occurences(word, words):
    words = [x.lower() for x in words.split()]
    count_word = Counter(words)
    return count_word[word.lower()]

word = 'python'
words = 'Python Conferences python training python events'

print(count_occurences(word, words))