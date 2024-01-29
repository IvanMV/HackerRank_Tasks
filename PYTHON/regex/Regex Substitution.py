'''
You are given a text of N lines. The text contains && and || symbols.
Your task is to modify those symbols to the following:

&& → and
|| → or

Both && and || should have a space " " on both sides.
'''

import re

n = int(input())
for i in range(n):
    data = re.sub(r'(?<=\s)(&&)(?=\s)', 'and', input())
    data = re.sub(r'(?<=\s)(\|\|)(?=\s)', 'or', data)
    print(data)