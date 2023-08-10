'''
.symmetric_difference()

https://s3.amazonaws.com/hr-challenge-images/9421/1437912471-534f33cf60-AB.png

The .symmetric_difference() operator returns a set with all the elements that are in the set and the iterable but not both.
Sometimes, a ^ operator is used in place of the .symmetric_difference() tool, but it only operates on the set of elements in set.
The set is immutable to the .symmetric_difference() operation (or ^ operation).
'''

english_num = int(input())
english_set = set(map(int, input().split()))
french_num = int(input())
french_set = set(map(int, input().split()))
total_set = english_set.symmetric_difference(french_set)
print(len(total_set))