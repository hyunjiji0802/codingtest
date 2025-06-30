from itertools import permutations
N, M = map(int, input().split())
l = list(map(int, input().split()))
c = list(set(permutations(l,M)))
c.sort()
for i in c:
    if sorted(i) ==  list(i):
        print(*i)
