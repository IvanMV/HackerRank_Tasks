from collections import OrderedDict

n = int(input())
purchase = OrderedDict()

for i in range(n):
    temp = input().split()
    net_price  = int(temp.pop())
    item_name  = ' '.join(temp)
    if item_name not in purchase:
        purchase[item_name] = net_price
    else:
        purchase[item_name] += net_price

for item in purchase.items():
    print(*item)