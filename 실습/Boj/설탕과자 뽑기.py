h, w = map(int,input().split())
grid = [[0 for _ in range(w)] for _ in range(h)]

n = int(input())
for _ in range(n):
    l, d, x, y = map(int, input().split())

    if d == 0:
        for i in range(y-1, y-1+l):
            # print(x-1, i)
            grid[x-1][i] = 1
    if d == 1:
        for j in range(x-1, x-1+l):
            # print(j, y-1)
            grid[j][y-1] = 1

for g in grid:
    print(*g)