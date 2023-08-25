from collections import defaultdict

n, m = map(int, input().split())

first_group = []
for i in range(n):
    first_group.append(input())
    
second_group = []
for i in range(m):
    second_group.append(input())
    
my_dict = defaultdict(list)

for key in second_group:
    if key not in my_dict:
        num = 0
        for item in first_group:
            num += 1
            if key == item:
                my_dict[key].append(num)
        if key not in first_group:
            my_dict[key].append(-1)

for key in second_group:
    print(*my_dict[key])
