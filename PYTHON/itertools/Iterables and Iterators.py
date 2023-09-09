from itertools import combinations, groupby


# Read from input
n = int(input())
data = input().split()
k = int(input())


# Task
comb = list(combinations(data, k))
total_comb = len(comb)
x = 0
for i in comb:
    if 'a' in i:
        x += 1
result = x / total_comb


# Result output
print(result)