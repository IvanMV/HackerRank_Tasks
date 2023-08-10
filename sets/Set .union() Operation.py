'''
.union()

The .union() operator returns the union of a set and the set of elements in an iterable.
Sometimes, the | operator is used in place of .union() operator, but it operates only on the set of elements in set.
Set is immutable to the .union() operation (or | operation).
'''


english_num = int(input())
english_set = set(map(int, input().split()))
french_num = int(input())
french_set = set(map(int, input().split()))
total_set = english_set.union(french_set)
print(len(total_set))
