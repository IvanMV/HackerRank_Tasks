'''
.difference()

https://s3.amazonaws.com/hr-challenge-images/9420/1437904659-11e4bef847-A-B.png

The tool .difference() returns a set with all the elements from the set that are not in an iterable.
Sometimes the - operator is used in place of the .difference() tool, but it only operates on the set of elements in set.
Set is immutable to the .difference() operation (or the - operation).
'''

english_num = int(input())
english_set = set(map(int, input().split()))
french_num = int(input())
french_set = set(map(int, input().split()))
total_set = english_set.difference(french_set)
print(len(total_set))