from collections import defaultdict

n, m = map(int, input().split())

A = []
for i in range(n):
    A.append(input())
    
B = []
for i in range(m):
    B.append(input())
    
my_dict = defaultdict(list)

for key in B:
    if key not in my_dict:
        num = 0
        for item in A:
            num += 1
            if key == item:
                my_dict[key].append(num)
        if key not in A:
            my_dict[key].append(-1)

for key in B:
    print(*my_dict[key])
