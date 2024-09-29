import sys
from collections import deque
n = int(sys.stdin.readline())
matrix = []
rain_set = set()
for i in range(n):
    tmp = list(map(int,sys.stdin.readline().rstrip().split()))
    for j in tmp:
        rain_set.add(j)
    matrix.append((tmp))

    #상 하 좌 우
dc = [0,0,-1,1]
dr = [-1,1,0,0]
def bfs(start_r,start_c,rain,visited):
    q = deque([(start_r,start_c)]) #비의 양 높이 부터 탐색
    visited[start_r][start_c] = True #방문처리
    while q: #큐가 빌 때 까지
        cur_r,cur_c = q.popleft()
        for i in range(4):
            nr, nc = cur_r+dr[i], cur_c+dc[i]
            if 0<=nr<n and 0<=nc<n and visited[nr][nc] is False and matrix[nr][nc]>rain: #방문하지않았으며 물에 잠기는 높이가 아니면
                visited[nr][nc]=True
                q.append((nr,nc))

max영역 = 1 #비가 안오면 아무것도 안잠기므로 영역은 하나
for rain in list(rain_set):
    영역=0
    visited = [[False for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if matrix[r][c]>rain and visited[r][c] is False: #비의 양
                bfs(r,c,rain,visited)
                영역+=1
    max영역 = max(max영역,영역)
print(max영역)