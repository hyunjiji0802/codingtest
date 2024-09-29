import sys
from collections import deque
m,n,h = map(int,sys.stdin.readline().rstrip().split())
box = []
q = deque([])
total_tomato = 0
riped_tomato = 0

for height in range(h):
    floor = [[int(i) for i in sys.stdin.readline().rstrip().split()]for j in range(n)]
    for row in floor:
        for item in row:
            if item == 0 or item == 1:
                total_tomato +=1 #전체 토마토 수 세기
            if item ==1:
                riped_tomato +=1 #익은 토마토 수 세기 ->bfs 탐색 후 전체 토마토 수와 익은 토마토 수가 같으면 날짜 반환, 그렇지 않으면 모두 익지 못했으므로 -1 반환
    box.append(floor)

    #상 하 좌 우 위 아래
dm = [0,0,-1,1,0,0]
dn = [-1,1,0,0,0,0]
dh = [0,0,0,0,1,-1]

def bfs(m,n,h):
    global total_tomato, riped_tomato
    days = 0
    visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]
    q = deque()

    for ch in range(h):
        for cn in range(n):
            for cm in range(m):
                if box[ch][cn][cm] == 1:
                    q.append((ch, cn, cm, days)) #익은 토마토 큐에 추가 - (m,n,h,날짜)
                    visited[ch][cn][cm] = True #방문표시

    while q:
        ch,cn,cm,days =q.popleft()
        for i in range(6):
            nm,nn,nh = cm+dm[i], cn+dn[i],ch+dh[i]
            if 0<=nm<m and 0<=nn<n and 0<=nh<h and box[nh][nn][nm] == 0 and visited[nh][nn][nm] == False: #주변에 안익은 토마토가 있으면
                visited[nh][nn][nm] = True #토마토 익히고 방문처리
                riped_tomato +=1
                q.append((nh,nn,nm,days+1)) #큐에 삽입

    if total_tomato == riped_tomato: #토마토가 다 익었으면
        return days
    else:
        return -1 #안익었으면 -1 반환


print(bfs(m,n,h))