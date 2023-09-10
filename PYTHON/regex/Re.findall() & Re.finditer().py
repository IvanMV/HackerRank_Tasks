import re

pattern = re.compile(r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])[AEIOUaeiou]{2,}(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])')
match = pattern.findall(input())
if match:
    for i in match:
        print(i)
else:
    print('-1')
