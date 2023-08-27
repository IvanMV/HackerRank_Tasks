from collections import deque

n = int(input())
d = deque()
for i in range(n):
    data = input().split()
    if len(data) == 2:
        command = data[0]
        value = int(data[1])
    else:
        command = data[0]
    if command == 'append':
        d.append(value)
    elif command == 'appendleft':
        d.appendleft(value)
    elif command == 'pop':
        d.pop()
    elif command == 'popleft':
        d.popleft()
print(*d)