from sys import stdin


x = list(stdin)
sum_chi= 0
count_nechi = 0
for i in x:
    try:
        sum_chi += int(i)
    except ValueError:
        try:
            sum_chi += float(i)
        except ValueError:
            count_nechi += 1
print(sum_chi, count_nechi, sep = '\n')