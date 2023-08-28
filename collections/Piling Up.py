'''
Задание: создать из последовательности чисел пирамиду, снизу вверх, где нижний блок 
должен быть >= блоку сверху. Можно брать для укладки только левое или правое число из последовательности.
Если пирамиду можно сложить по указанным условиям, вывести 'Yes', в противном случае 'No'
n - число кейсов
'''

from collections import deque

n = int(input())

for i in range(n):
    num = int(input())
    dq = deque(map(int, input().split()), num)
    last = None
    while dq:
        m = len(dq)
        if dq[0] >= dq[m-1]:
            if not last:
                last = dq.popleft()
            else:
                if last >= dq[0]:
                    last = dq.popleft()
                else:
                    print('No')
                    break
            continue
        elif dq[m-1] > dq[0]:
            if not last:
                last = dq.pop()
            else:
                if last >= dq[m-1]:
                    last = dq.pop()
                else:
                    print('No')
                    break
            continue
    if not dq:
        print('Yes')