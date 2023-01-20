from collections import Counter

books = Counter(map(int, input().split()))
su = 0
for i in range(int(input())):
    uch = list(map(int, input().split()))
    if uch[0] in books.keys() and books[uch[0]] > 0:
        su += uch[1]
        books[uch[0]] -= 1

print(su)
