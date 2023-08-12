a = set(map(int, input().split()))
n = int(input())
result = 'True'
for i in range(n):
    temp = set(map(int, input().split()))
    if not a.issuperset(temp):
        result = 'False'
        break
print(result)