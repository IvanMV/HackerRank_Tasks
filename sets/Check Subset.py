total = int(input()) # total number of cases


for i in range(total):
    input()
    a = set(map(int, input().split()))
    input()
    b = set(map(int, input().split()))
    if a.issubset(b):
        print('True')
    else:
        print('False')