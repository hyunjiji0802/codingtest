l = []
for _ in range(19):
    l.append(list(map(int, input().split())))
N = int(input())
for _ in range(N):
    r, c = map(int, input().split())

    for i in range(19):
        if l[r-1][i] == 0: l[r-1][i] = 1
        else: l[r-1][i] = 0

    for j in range(19):
        if l[j][c-1] == 0: l[j][c-1] = 1
        else: l[j][c-1] = 0

for line in l:
    print(*line)
print()
