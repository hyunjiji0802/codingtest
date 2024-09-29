import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
tree = [[] for _ in range(n)] #-1 0 0 2 2 4 4 6 6 입력 -> 그래프 저장 [[1, 2], [], [3, 4], [], [5, 6], [], [7, 8], [], []]

for node_num,i in enumerate(sys.stdin.readline().rstrip().split()):
    if int(i)==-1 : continue
    tree[int(i)].append(node_num) #트리 노드 초기회
r = int(sys.stdin.readline().rstrip())

leaf_list = [] #리프 노드 리스트

def remove_tree(tree,r): #노드 제거
    stack = deque([(r)]) #제거 할 노드부터 탐색하기, 스택에 제거할 노드 추가
    while stack:
        cn = stack.pop()
        while tree[cn]: #해당 노드 아래로 연결된 노드들을 모두 제거할 때 까지
            nn = tree[cn].pop()
            stack.append(nn) #제거와 동시에 스택에 push
        for node in tree: #만약 트리 내에 제거할 노드 위 연결된 노드가 있으면. 연결된 노드에서도 해당 노드 제거 (0-1 연결되었을 때, 제거 할 노드가 1이면 -> [[1],[]] 에서 1과 연결된 노드인 0에서 원소 1 제거 -> [[],[]]
            if cn in node:
                node.remove(cn)
        tree[cn].append(-100) #쓰레기값 넣기(나중에 리프노드 계산 때 편리하게 하기 위함, 리프 노드는 len(node)가 0임. 노드와 연결된 원소를 모두 pop해서 똑같이 길이가 0이므로 하나 추가하기)

    for node_num, node in enumerate(tree):
        if len(node) == 0:
            leaf_list.append(node_num)
    return len(leaf_list)

print(remove_tree(tree,r))
