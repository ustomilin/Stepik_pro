from collections import Counter
from sys import stdin

def uch_bal(text):
    text = Counter(text)
    print(text.most_common()[-2][0])

sl = {}
for i in stdin:
    j  = i.strip().split()
    sl[j[0]] = int(j[1])
uch_bal(sl)
