'''
You are given a string S.
Your task is to find the first occurrence of an alphanumeric character in S
(read from left to right) that has consecutive repetitions.
'''
import re

pattern = re.compile(r'([A-Za-z0-9])\1{1}')
match = re.search(pattern, input())
print(match.group(1) if match else '-1')

'''
Создаем объект паттерна регулярного выражения с помощью re.compile(). 
Паттерн в данном случае это регулярное выражение r'([A-Za-z0-9])\1{1}'.
([A-Za-z0-9]): Эта часть определяет группу захвата.
\1{1}: Эта часть означает, что символ, найденный в группе захвата, должен повторяться ровно один раз. 
  \1 обозначает повторение первой группы захвата, и 
  {1} указывает, что это повторение должно произойти один раз.
'''