import sys

n = int(sys.stdin.readline())
tree =[[] for _ in range(n+1)]
for _ in range(n-1):
    n1,n2 = map(int,sys.stdin.readline().rstrip().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

def dfs(node_num, l, visited):
    visited[node_num]=True

    if 1 in tree[node_num]:
        return l
    next_nums = tree[node_num]
    for num in next_nums:
        if visited[num]==False:
            visited[num]=True
            l.append(node_num)
            dfs(num, l,visited)

for node_num in range(2,n):
    visited = [False for _ in range(n+1)]
    l = [node_num]
    dfs_result = node_num,dfs(node_num,l, visited)
    print("결과",dfs_result)
