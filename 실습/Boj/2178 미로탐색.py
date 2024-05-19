from collections import deque
n,m = map(int,input().split())
maze = [[0 for _ in range(m+1)]]
stack = []

for i in range(n): #미로 생성
    n_list = list(input())
    for j in range(len(n_list)):
        n_list[j] = int(n_list[j])
    maze.append([0]+n_list)

    #상 하 좌 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
    q = deque([(x, y)]) #내부에 튜플 처리 안하면 반복 불가능한 int객체의 압축을 풀 수 없다는 에러 나옴
    while q: #큐가 빌 때 까지
        x, y  = q.popleft() #현재 좌표 꺼내서
        for i in range(4): #네 방향으로 갈 수 있는지 탐색
            next_x, next_y = x + dx[i], y + dy[i] #각 방향 이동 후 좌표
            if 1 <= next_x <= n and 1 <= next_y <= m and maze[next_x][next_y] == 1: #범위 내에 있고, 갈 수 있으면
                maze[next_x][next_y] = maze[x][y] + 1 #현재 이동 거리+1을 다음 이동 좌표에 저장
                q.append((next_x, next_y)) #이동 후 큐에 삽입

        # print(q)
        # print()
        # for z in maze:
        #     print(z)
    return maze[n][m]

#(1, 1) 부터 시작
print(bfs(1, 1))


