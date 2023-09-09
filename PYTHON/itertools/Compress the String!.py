from itertools import groupby

data = input()
g_list = []
for k, g in groupby(data):
    g_list.append(list(g))
shorten = []
for x in g_list:
    shorten.append((len(x), int(x[0])))  
print(*shorten)