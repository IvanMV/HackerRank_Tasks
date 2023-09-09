'''
.intersection()

https://s3.amazonaws.com/hr-challenge-images/9419/1437830945-a56a63892c-AB.png

The .intersection() operator returns the intersection of a set and the set of elements in an iterable.
Sometimes, the & operator is used in place of the .intersection() operator, but it only operates on the set of elements in set.
The set is immutable to the .intersection() operation (or & operation).
'''

english_num = int(input())
english_set = set(map(int, input().split()))
french_num = int(input())
french_set = set(map(int, input().split()))
total_set = english_set.intersection(french_set)
print(len(total_set))