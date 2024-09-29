import sys
n,m = map(int,sys.stdin.readline().rstrip().split())
total_cost = 0 #전체 비용 계산
save_cost = 0 #모든 건물만 연결하는 최소 비용 계산
parents = [i for i in range(n+1)] #각 노드의 부모는 자기 자신으로 초기화
rank = [0] * (n + 1)  # 랭크 배열
linked_road = 0
costs = []
for _ in range(m):
    m1,m2,cost = map(int,sys.stdin.readline().rstrip().split())
    total_cost+=cost
    costs.append([m1,m2,cost])

costs.sort(key=lambda x:x[2]) #간선의 가중치를 오름차순 정렬

def find(parent, x): #부모 구하기
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, m1, m2): #부모 합치기
    root1 = find(parent, m1)
    root2 = find(parent, m2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        elif rank[root1] < rank[root2]:
            parent[root1] = root2
        else:
            parent[root2] = root1
            rank[root1] += 1

for m1,m2,cost in costs: #크루스칼 알고리즘 - 최소 신장트리 구하기 union & find
    if linked_road==n-1: #도로 수가 전체 건물 수 - 1이면 종료조건
        break
    if find(parents, m1) != find(parents,m2): #두 노드가 같은 집합에 속하지 않으면

        union(parents,rank,m1,m2)
        save_cost+=cost
        linked_road+=1

if linked_road!=n-1: #for문 다 돌고 linked_road가 처음 간선 수와 같으면 *(최소신장트리가 아니므로) -1 출력, 또한 total_coat와 save_cost가 같으면 그래프 연결이 되지 않았음. 따라서 -1 출력
    print(-1)
else:
    print(total_cost-save_cost)