"""
input data

3 4
0 1 0 0
0 0 0 0
0 0 1 0

"""


n, m = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
newl = [(i,j) for i in range(n) for j in range(m) if l[i][j]== 1]

print(l)
print(newl)

"""
[[0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0]]
[(0, 1), (2, 2)]
"""