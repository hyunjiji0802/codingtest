import sys
from collections import deque

n,m = map(int,sys.stdin.readline().rstrip().split())
maze = [[int(i) for i in sys.stdin.readline().rstrip()] for _ in range(n)]

    #상 하 좌 우
dc = [0,0,-1,1]
dr = [-1,1,0,0]

def bfs(n, m):
    q = deque([(0,0,0,1)]) #r,c,벽 부쉈는지 아닌지,이동 거리
    visited = [[[False]*2 for _ in range(m)] for _ in range(n)] #0은 벽 부수지 X 방문표시, 1은 벽 부쉈을 때 방문표시
    visited[0][0][0] =True
    while q:
        r, c, broken, d = q.popleft()
        # 목적지 도달 시 경로 길이 반환
        if r == n - 1 and c == m - 1:
            return d
        # 4방향 이동
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            # 맵의 범위를 벗어나지 않고 방문하지 않은 경우
            if 0 <= nr < n and 0 <= nc < m :
                # 이동할 곳이 벽이 아니고 방문기록에 없을 때(벽 부쉈거나 부수지 않았거나 ->broken으로 확인)
                if maze[nr][nc] == 0 and not visited[nr][nc][broken]:
                    visited[nr][nc][broken] = True #좌표 방문처리
                    q.append((nr, nc, broken, d + 1))
                # 이동할 곳이 벽이고 벽을 부수지 않았으며 방문하지 않은 경우 (벽을 부수지 않은 상태에서만 벽을 부수고 이동 가능)
                elif maze[nr][nc] == 1 and broken == 0 and not visited[nr][nc][1] :
                    visited[nr][nc][1] = True #벽 좌표 방문처리(벽 부숨)
                    q.append((nr, nc, 1, d + 1))

    # 큐가 빌 때까지 목적지에 도달하지 못한 경우 -1 반환
    return -1

print(bfs(n,m))