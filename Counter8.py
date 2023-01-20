from collections import Counter

data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')

data.min_values = lambda: list(filter(lambda i: i[1] == min(data.values()), data.items()))
data.max_values = lambda: list(filter(lambda i: i[1] == max(data.values()), data.items()))

print(data.max_values())