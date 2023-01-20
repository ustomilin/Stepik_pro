from collections import Counter

books = Counter(map(int, input().split()))
total = 0
for _ in range(int(input())):
    uch = list(map(int, input().split()))
    if books[uch[0]] > 0:
        total += uch[1]
        books[uch[0]] -= 1

print(total)
