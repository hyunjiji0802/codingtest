from collections import deque
import sys
n = int(sys.stdin.readline().rstrip())
paint = [[i for i in sys.stdin.readline().rstrip()] for _ in range(n)] #그림 입력
rd_paint=[]
for p in paint:
    rd_paint.append(list(''.join(p).replace('G','R')))

normal_group, rd_group = 0,0
    #상 하 좌 우
dc = [0,0,-1,1]
dr = [-1,1,0,0]

def dfs_normal(r,c):
    stack= deque([(r,c)])
    while stack:
        cur_r,cur_c = stack.pop()
        color = paint[cur_r][cur_c]
        paint[cur_r][cur_c] = 'X'  # 현재 위치 방문표시
        for i in range(4):
            nr, nc = cur_r+dr[i], cur_c+dc[i]
            if 0<=nr<n and 0<=nc<n and paint[nr][nc] == color and paint[nr][nc] !='X': #범위 내에 있고,현재 색상과 같으며 방문한 곳이 아니면
                stack.append((nr,nc)) #스택에 넣기

def dfs_rd(r,c):
    stack= deque([(r,c)])
    while stack:
        cur_r,cur_c = stack.pop()
        color = rd_paint[cur_r][cur_c]
        rd_paint[cur_r][cur_c] = 'X'  # 현재 위치 방문표시
        for i in range(4):
            nr, nc = cur_r+dr[i], cur_c+dc[i]
            if 0<=nr<n and 0<=nc<n and rd_paint[nr][nc] == color and rd_paint[nr][nc] !='X': #범위 내에 있고,현재 색상과 같으며 방문한 곳이 아니면
                stack.append((nr,nc)) #스택에 넣기

for r in range(n): #정상인 그림 dfs
    for c in range(n):
        if paint[r][c] != 'X': #방문한 곳 아니면
            dfs_normal(r,c)
            normal_group +=1

for r in range(n): #적록색약 그림 dfs
    for c in range(n):
        if rd_paint[r][c] != 'X': #방문한 곳 아니면
            dfs_rd(r,c)
            rd_group +=1

print(normal_group, rd_group)