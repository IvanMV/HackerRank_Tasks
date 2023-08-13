from itertools import combinations_with_replacement

data = input().split()
string = ''.join(sorted(data[0]))
k = int(data[1])

comb = combinations_with_replacement(string, k)
for x in comb:
    print(*x, sep = '')