'''
You are given a space separated list of integers. 
If all the integers are positive, then you need to check if any integer is a palindromic integer.
Can you solve this challenge in 3 lines of code or less?
'''

n, data = int(input()), tuple(input().split())
print('True') if all(int(x) >0  for x in data) and any(i == ''.join(reversed(i)) for i in data) else print('False')