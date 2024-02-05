import re

pattern = re.compile(r'(?<=[^\\n]{1})#[A-Fa-f0-9]{6}|(?<=[^\\n]{1})#[A-Fa-f0-9]{3}(?=\W)')

n = int(input())
for _ in range(n):
    line = input()
    data = re.findall(pattern, line)
    if data:
        for i in data:
            print(i)