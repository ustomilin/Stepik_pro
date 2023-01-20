from collections import Counter
import csv

with open('/files/name_log.csv', encoding='utf8') as file:
    text = csv.reader(file)
    print(text)