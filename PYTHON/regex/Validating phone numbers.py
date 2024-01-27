# A valid mobile number is a ten digit number starting with a 7, 8, 9.

import re

n = int(input())
for i in range(n):
    string = input()
    pattern = r'(^[789]){1}([0-9]){9}\b'
    result = re.match(pattern, string)
    if result:
        print('YES')
    else:
        print('NO')