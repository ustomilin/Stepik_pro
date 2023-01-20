import csv
import json

with open('files/prices.json', encoding='utf8') as prices, open('files/quarter1.csv', encoding='utf8') as q1, open(
        'files/quarter2.csv', encoding='utf8') as q2, open('files/quarter3.csv', encoding='utf8') as q3, open(
        'files/quarter4.csv', encoding='utf8') as q4:
    prices = json.load(prices)
    q1 = list(csv.reader(q1))
    del q1[0]
    d = {}
    for i in q1:
        d[i[0]] = int(i[1]) + int(i[2]) + int(i[3])
    q2 = list(csv.reader(q2))
    del q2[0]
    for i in q2:
        d[i[0]] += int(i[1]) + int(i[2]) + int(i[3])
    q3 = list(csv.reader(q3))
    del q3[0]
    for i in q3:
        d[i[0]] += int(i[1]) + int(i[2]) + int(i[3])
    q4 = list(csv.reader(q4))
    del q4[0]
    for i in q4:
        d[i[0]] += int(i[1]) + int(i[2]) + int(i[3])
    su = 0
    for i, j in d.items():
        su += prices[i] * j
    print(su)
