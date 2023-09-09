from collections import namedtuple

n = int(input())
string = ','.join(input().split())

Data = namedtuple('Data', string)
marks_sum = 0

for i in range(n):
    inp = input().split()
    temp = Data(inp[0], inp[1], inp[2], inp[3])
    marks_sum += int(temp.MARKS)
    
avr = marks_sum / n

print(round(avr, 2))