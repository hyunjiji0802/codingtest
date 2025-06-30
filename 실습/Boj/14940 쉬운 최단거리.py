from collections import deque

N, M  = map(int, input().split())
l = list()
start = []
for r in range(N):
    tmp = list(map(int, input().split()))
    l.append(tmp)

    # 시작지점 저장
    if 2 in tmp:
        start = [r, tmp.index(2)]

visited = [[False for _ in range(M)] for _ in range(N)]

# 상 하 좌 우
d = [(-1,0), (1,0), (0,-1), (0,1)]
q = deque([start])

def bfs():
    while q:
        if len(q) == 0: #큐가 비어있으면
            return q, l

        else:
            cur_r, cur_c = q.popleft()

        for dr, dc in d:
            next_r, next_c = cur_r + dr, cur_c + dc
            if 0<= next_r < N and 0<= next_c < M and l[next_r][next_c] == 1 and visited[next_r][next_c] == False:
                q.append([next_r, next_c])
                visited[next_r][next_c] = True
                l[next_r][next_c] = l[cur_r][cur_c] + 1

l[start[0]][start[1]] = 0
bfs()


for i in range(N):
    for j in range(M):
        if visited[i][j] == False and l[i][j] == 1:
            l[i][j] = -1

for k in l:
    print(*k)
print()


# from sys import stdin
# from collections import deque
# N,M = map(int,stdin.readline().rstrip().split())
# arr = []
# visited = [list(-1 for _ in range(M)) for _ in range(N)]
# # 상하좌우
# dr = [-1,1,0,0]
# dc = [0,0,-1,1]
#
# #시작 위치 담음
# start_r, start_c = 0,0
# for n in range(N):
#     tmp = list(map(int,stdin.readline().rstrip().split()))
#     if 2 in tmp:
#         start_r = n
#         start_c = tmp.index(2)
#     arr.append(tmp)
#
# def bfs(arr, start_r, start_c):
#     # 시작지점 방문표시
#     visited[start_r][start_c] = 0
#     q = deque([(start_r,start_c)])
#
#     while q:
#         cur_r,cur_c = q.popleft()
#
#         for r,c in zip(dr,dc):
#             next_r = cur_r+r
#             next_c = cur_c+c
#
#             if 0<=next_r<len(arr) and 0<=next_c<len(arr[0]) and visited[next_r][next_c] == -1 :
#                 if arr[next_r][next_c] == 1:
#                     visited[next_r][next_c] = visited[cur_r][cur_c] + 1
#                     q.append((next_r, next_c))
#                 if arr[next_r][next_c] == 0:
#                     visited[next_r][next_c] = 0
#
#     return visited
#
# visited = bfs(arr, start_r, start_c)
#
# # for m in visited:
# #     print(*m)
# # print()
#
# for r in range(N):
#     for c in range(M):
#         if arr[r][c] == 0:  # 갈 수 없는 땅은 0
#             visited[r][c] = 0
#     print(*visited[r])
