import sys
from collections import deque

n,m = map(int, sys.stdin.readline().rstrip().split())
#인접 리스트
n_list = [[] for _ in range(n)]

for _ in range(n-1):
    n1,n2,dist = map(int, sys.stdin.readline().rstrip().split())
    n1-=1 #1부터 시작, 인덱스는 0부터 시작이라 1씩 빼고 저장
    n2-=1

    n_list[n1].append((n2,dist)) #연결 노드 리스트 저장
    n_list[n2].append((n1,dist))

def bfs(s,e,dist,visited):
    q = deque([(s,dist)])
    while q: #큐가 모두 빌 때 까지
        cur_n,dist = q.popleft() #현재 위치 pop
        visited[cur_n] = True #방문처리
        if cur_n == e: #목적지면 현재 거리 반환
            return dist

        for nd,d in n_list[cur_n]:
            if visited[nd]==False: #방문한 노드가 아니면
                visited[nd]=True #방문처리
                q.append((nd,dist+d)) #거리 추가

for _ in range(m):#거리를 알고싶은 노드 쌍 입력
    dist = 0
    visited = [False for _ in range(n)]
    n1,n2 = map(int, sys.stdin.readline().rstrip().split())
    print(bfs(n1-1,n2-1,dist,visited))
