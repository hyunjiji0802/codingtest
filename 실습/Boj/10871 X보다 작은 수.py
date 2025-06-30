N, M = map(int, input().split())

l = list(map(int, input().split()))

m = []
for i in l:
    if i < M:
        m.append(i)
print(*m)