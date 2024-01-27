import re

n = int(input())

for i in range(n):
    data = tuple(input().split())
    pattern = r'<([A-Za-z]){1}([\.\w-]+)@([A-Za-z]+)\.([A-Za-z]{1,3})>'
    result = re.match(pattern, data[1])
    if result:
        print(f'{data[0]} {data[1]}')