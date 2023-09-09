students, subjects = map(int, input().split())

marks = []

for _ in range(subjects):
    temp = tuple(map(float, input().split()))
    marks.append(temp)
    
grouped_marks = zip(*marks)

for i in grouped_marks:
    print(sum(i) / subjects)