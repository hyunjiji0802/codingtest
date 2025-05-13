from collections import defaultdict, deque
N, M = map(int, input().split())
d = defaultdict(list)
q = deque()
degree = [0 for _ in range(N+1)]
l = [0 for _ in range(N+1)]

for i in range(N):
    d[i]

for _ in range(M):
    a,b = map(int,input().split())
    d[a].append(b) #b의 선수과목 a
    degree[b] += 1 #b의 차수 +1

for i in range(1,N+1):
    if degree[i] == 0:
        q.append(i)
    l[i] = 1

while q:
    cur = q.pop()
    for next in d[cur]:
        #진입 차수 감소
        degree[next]-=1
        #학기 수 갱신 (현재 학기보다 1 증가)
        l[next] = max(l[next], l[cur] + 1)
        #진입차수 0이면 큐에 추가
        if degree[next] == 0:
            q.append(next)

print(*l[1:])
