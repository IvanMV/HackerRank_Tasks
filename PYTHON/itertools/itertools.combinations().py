from itertools import combinations

data = input().split()
string = ''.join(sorted(data[0]))
k = int(data[1])

for i in range(1, k+1):
    comb = combinations(string, i)
    for x in comb:
        print(*x, sep = '')
    