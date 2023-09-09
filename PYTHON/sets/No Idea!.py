nm = input().split('')
n = nm[0]
m = nm[1]

my_array = input().split('')
a = set(input().split(''))
b = set(input().split(''))

happy = 0

for i in my_array:
    if i in a:
        happy += 1
    if i in b:
        happy -= 1
        
print(happy)