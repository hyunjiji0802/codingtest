import sys
input = sys.stdin.readline

n,m = map(int,input().split())
n_list = [[] for _ in range(n+1)]
count=0
visited = [False for _ in range(n+1)]
visited[0] = True
for _ in range(m):
    n1,n2 = map(int,input().split())
    n_list[n1].append(n2)
    n_list[n2].append(n1)

def dfs(i):
    stack = [n_list[i]]  # i번 정점 탐색
    while stack:
        l = stack.pop()
        while len(l)>0: #연결된 노드의 인접 리스트가 비어있지 않으면, 즉 다른 노드와 연결되어있으면
                next_n = l.pop() #하나 꺼내서 스택에 넣기
                if not visited[next_n]: #첫방문이면
                    visited[next_n] = True #방문 리스트에 방문 표시
                    stack.append(n_list[next_n])
                # elif visited[next_n] and len(n_list[next_n])>0: #방문 했던 노드면
                #     pass
    return True
i = 1 #첫 정점부터 탐색
while i<=n and not all(visited): #모든 정점을 방문할 때 까지
    if not visited[i]: #첫방문이면
        visited[i] = True # i번 정점 방문 표시
        isgrouped = dfs(i) # True 반환이면 count+1 false면 -1
        count+=1 if isgrouped else -1
    #이미 탐색한 정점은 보지 않음
    i+=1

print(count)
