m_count = int(input())
m = input().split()
m = list(map(int, m))
m = set(m)

n_count = int(input())
n = input().split()
n = list(map(int, n))
n = set(n)

m_dif = m.difference(n)
n_dif = n.difference(m)

united = m_dif.union(n_dif)

for i in sorted(united):
    print(i)