'''
Найти все пересекающиеся вхождения подстроки в строке
'''

import re

s = input()
pattern = re.compile(input())
result = True
start = 0
while result!= None:
    result = re.search(pattern, s[start:])
    if result:
        print((result.start() + start, result.end() + start - 1))
        if result.end() + start == len(s):
            break
        elif result.start() == 0:
            start += 1
        else:
            start = result.start() + start + 1
    else:
        if start == 0:
            print((-1, -1))