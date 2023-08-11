a_num = int(input()) # number of elements in set A
a_set = set(map(int, input().split())) # space separated list of elements in set
n_num = int(input()) # number of other sets
for i in range(n_num):
    line = input().split()
    temp_set = set(map(int, input().split()))
    if line[0] == 'update':
        a_set.update(temp_set)
    elif line[0] == 'intersection_update':
        a_set.intersection_update(temp_set)
    elif line[0] == 'symmetric_difference_update':
        a_set.symmetric_difference_update(temp_set)
    elif line[0] == 'difference_update':
        a_set.difference_update(temp_set)
print(sum(a_set))