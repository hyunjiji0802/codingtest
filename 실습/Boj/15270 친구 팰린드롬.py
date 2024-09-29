import sys
n,m = map(int,sys.stdin.readline().rstrip().split())
r = [[] for _ in range(n+1)]
for _ in range(m):
    n1,n2 = map(int,sys.stdin.readline().rstrip().split())
    r[n1].append(n2)
    r[n2].append(n1)

match = [0 for _ in range(n+1)]
max_match = 0 #최대 춤 출 수 있는 친구 수

def dfs(v,visited): #친구가 연결될 수 있는지 모든 노드 탐색
    for u in r[v]:
        if visited[u]: #해당 친구 방문했으면 continue
            continue
        else:
            visited[u] = True #방문 안했으면 방문처리
            visited[v] = True
        if match[u] == 0 or dfs(match[u],visited): #친구 연결이 안됐으면 / 이미 된 경우인데 다른 친구랑 연결이 가능하면
            match[u] = v
            match[v] = u #서로 연결하기
            # print(u,v)
            return True
    return False #모두하고도 연결이 안되면 false 반환

for v in range(1,n+1):
    if match[v]== 0: #연결된 친구가 없으면
        visited = [False for _ in range(n+1)] #매 탐색마다 방문 배열 초기화
        if dfs(v,visited): #매칭되었으면 (true 반환)
            max_match +=2 #연결 친구 추가 (1쌍)

if n - max_match > 0:  # 모든 친구들이 연결되지 않았다면
    print(max_match + 1)  # 가운데 로봇 춤 친구 하나 더하기
else:
    print(max_match)
