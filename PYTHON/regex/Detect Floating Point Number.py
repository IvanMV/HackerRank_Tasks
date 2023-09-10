import re


t = int(input())
pattern = r'^([+]|[-]){0,1}\d*\.{1}\d+$'


for _ in range(t):
    s = input()
    match = re.search(pattern, s)
    if match:
        print('True')
    else:
        print('False')