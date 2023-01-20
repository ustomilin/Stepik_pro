from collections import Counter
import csv

with open('files/name_log.csv', encoding='utf8') as file:
    text = list(csv.reader(file))
    del text[0]
    text = list(map(lambda x: x[1], text))
    c = Counter(text)
    for email, count in sorted(c.items()):
        print(f'{email}: {count}')
