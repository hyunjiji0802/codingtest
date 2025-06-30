# 방향 벡터 : 좌, 우, 상, 하
dx = [-1, 1, 0, 0]  # x축(행)
dy = [0, 0, -1, 1]  # y축(열)


# DFS
def dfs(x, y):
    # 1. 현재 위치 방문 표시
    visited[x][y] = True

    print(f"({x}, {y})", end=' ')  # 탐색 순서 확인

    # 2. 상하좌우 탐색
    for dir in range(4):
        nx = x + dx[dir]  # 이동 후의 x 좌표
        ny = y + dy[dir]  # 이동 후의 y 좌표

        # 3. 좌표가 배열 범위 내에 있는지 확인
        if 0 <= nx < n and 0 <= ny < m:
            # 4. 다음 위치 방문 안했고 탐색 가능한 곳(1)인지 확인
            if not visited[nx][ny] and graph[nx][ny] == 1:
                # 5. 조건을 만족하면 DFS 재귀 호출로 깊이 탐색
                dfs(nx, ny)


# 전체 배열 크기 정의 (n: 행, m: 열)
n, m = len(graph), len(graph[0])

# 방문 여부 배열
visited = [[False] * m for _ in range(n)]

# DFS 시작 지점 호출 (예: dfs(0, 0))
dfs(, 시작y)
