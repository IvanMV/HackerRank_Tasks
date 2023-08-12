from math import sqrt, acos, degrees


# Input
ab = int(input())
bc = int(input())


# Сalculations
ac = sqrt(ab**2 + bc**2)
mc = ac/2
mb = mc
mbc_cos = degrees(acos((mb**2 + bc**2 - mc**2)/(2 * mb * bc)))
mbc_round = round(mbc_cos)


# Printing result
print(f'{mbc_round}\u00b0')