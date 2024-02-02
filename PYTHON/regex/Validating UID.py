'''
It must contain at least 2 uppercase English alphabet characters.
It must contain at least 3 digits.
It should only contain alphanumeric characters (A-Z, a-z  & 0-9).
No character should repeat.
There must be exactly 10 characters in a valid UID.
'''

import re

data = set()
pattern = re.compile(r'^(?=(?:[^A-Z]*[A-Z]){2})(?=(?:\D*\d){3})[A-Za-z0-9]{10}$')
n = int(input())
for _ in range(n):
    uid = input()
    if uid not in data:
        if re.match(pattern, uid) and len(set(uid)) == len(uid):
            print('Valid')
            data.add(uid)
        else:
            print('Invalid')
    else:
        print('Invalid') 